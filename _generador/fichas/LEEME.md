# Fichas de las guías con datos reales

- `fichas_pilares.py`: desayunos, café de especialidad, brunch, horario y cómo llegar (26/10/2026).
- `fichas_ola2.py`: almuerzo, sándwiches, postres, trabajar con laptop (27/10/2026).
- `carta-wasi.json`: la carta (nombre, precio, descripción, foto), sacada de `carta.html`.

Regla: precios y fotos SOLO de la carta del POS; «lo más pedido» SOLO de ventas reales;
nada que no conste (por ejemplo, enchufes). `foto()` falla si el producto no tiene foto.

Para regenerar tras un cambio de carta:

1. `node actualizar-carta.mjs` (refresca carta.html desde el POS).
2. Regenerar `carta-wasi.json` desde carta.html (cada línea `{"id":...,"items":[...]}` es una categoría).
3. `python3 fichas_pilares.py && python3 fichas_ola2.py` (escriben los .json).
4. `python3 ../generar.py fichas_pilares.json almuerzo.json mejoras.json` y luego `python3 ../registrar.py`.
