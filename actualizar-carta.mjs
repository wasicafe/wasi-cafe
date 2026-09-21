#!/usr/bin/env node
// Refresca, DENTRO de carta.html, la carta de respaldo (const D), el carrusel
// de promos (const PROMOS) y el bloque JSON-LD que lee Google, tomando los
// datos del POS (carta_publica). La página ya lee el POS en vivo en cada
// visita; esto mantiene al día lo que se ve sin JavaScript y lo que indexa
// Google. Se ejecuta a mano cuando cambian precios:
//
//   node actualizar-carta.mjs            # escribe los cambios
//   node actualizar-carta.mjs --ver      # solo muestra qué cambiaría
//
// Reutiliza el MISMO transformador que usa el navegador (el bloque marcado
// CARTA-EN-VIVO de carta.html), para que no puedan discrepar.
import { readFileSync, writeFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, join } from 'node:path'

const raiz = dirname(fileURLToPath(import.meta.url))
const ARCHIVO = join(raiz, 'version final de wasi', 'carta.html')
const soloVer = process.argv.includes('--ver')

const html = readFileSync(ARCHIVO, 'utf8')

/** El trozo entre `inicio` y el primer `;` tras el array que le sigue. */
function arrayLiteral(texto, inicio) {
  const i = texto.indexOf(inicio)
  if (i < 0) throw new Error(`no encontré ${inicio}`)
  const abre = texto.indexOf('[', i)
  let prof = 0
  for (let k = abre; k < texto.length; k++) {
    const ch = texto[k]
    if (ch === '[') prof++
    else if (ch === ']') { prof--; if (prof === 0) return { desde: i, hasta: k + 1, codigo: texto.slice(abre, k + 1) } }
  }
  throw new Error(`no cerró el array de ${inicio}`)
}

const dLit = arrayLiteral(html, 'const D=[')
const pLit = arrayLiteral(html, 'const PROMOS = [')
const D = eval(dLit.codigo)
const PROMOS = eval(pLit.codigo)

// El transformador vive una sola vez, en la página.
const ini = html.indexOf('/* CARTA-EN-VIVO-INICIO')
const fin = html.indexOf('/* CARTA-EN-VIVO-FIN */')
if (ini < 0 || fin < 0) throw new Error('no encontré el bloque CARTA-EN-VIVO en carta.html')
const transformador = new Function('D', 'PROMOS', 'document', 'fetch',
  html.slice(ini, fin) + '\nreturn { POS, cartaDesdePOS, promosDesdeCarta, menuSecciones };')
const { POS, cartaDesdePOS, promosDesdeCarta, menuSecciones } = transformador(D, PROMOS, undefined, undefined)

const r = await fetch(`${POS.url}/rest/v1/rpc/carta_publica`, {
  method: 'POST',
  headers: { apikey: POS.key, Authorization: `Bearer ${POS.key}`, 'Content-Type': 'application/json' },
  body: JSON.stringify({ p_slug: POS.slug }),
})
if (!r.ok) throw new Error(`el POS respondió ${r.status}`)
const data = await r.json()
const nueva = cartaDesdePOS(data, D)
if (nueva.length < 5) throw new Error('el POS devolvió una carta incompleta; no se toca el archivo')
const promos = promosDesdeCarta(nueva) ?? PROMOS

const antes = D.reduce((a, c) => a + c.items.length, 0)
const ahora = nueva.reduce((a, c) => a + c.items.length, 0)
const precioDe = (carta) => Object.fromEntries(carta.flatMap(c => c.items.map(i => [i.es.n, i.p])))
const pa = precioDe(D), pn = precioDe(nueva)
const cambios = Object.keys(pn).filter(n => pa[n] !== undefined && pa[n] !== pn[n])
const nuevos = Object.keys(pn).filter(n => pa[n] === undefined)
const fuera = Object.keys(pa).filter(n => pn[n] === undefined)
console.log(`categorías ${D.length} → ${nueva.length} · productos ${antes} → ${ahora}`)
if (cambios.length) console.log('precios que cambian:\n  ' + cambios.map(n => `${n}: S/ ${pa[n]} → S/ ${pn[n]}`).join('\n  '))
if (nuevos.length) console.log('entran: ' + nuevos.join(', '))
if (fuera.length) console.log('salen: ' + fuera.join(', '))
if (soloVer) process.exit(0)

const comoJs = (arr) => '[\n' + arr.map(x => JSON.stringify(x)).join(',\n') + '\n]'
let salida = html.slice(0, dLit.desde) + 'const D=' + comoJs(nueva) + html.slice(dLit.hasta)
const pLit2 = arrayLiteral(salida, 'const PROMOS = [')
salida = salida.slice(0, pLit2.desde) + 'const PROMOS = ' + comoJs(promos) + salida.slice(pLit2.hasta)

// JSON-LD: el bloque con "@type": "Menu".
const bloques = [...salida.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)]
let tocado = false
for (const b of bloques) {
  let j
  try { j = JSON.parse(b[1]) } catch { continue }
  if (j?.['@type'] !== 'Menu' || !j.hasMenuSection) continue
  j.hasMenuSection = menuSecciones(nueva)
  salida = salida.replace(b[0], `<script type="application/ld+json">\n${JSON.stringify(j, null, 1)}\n</script>`)
  tocado = true
  break
}
if (!tocado) throw new Error('no encontré el JSON-LD del menú')

writeFileSync(ARCHIVO, salida)
console.log(`carta.html actualizado (${(salida.length / 1024).toFixed(0)} KB). Revisa con git diff y sube a main para publicar.`)
