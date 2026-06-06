#!/usr/bin/env ruby
# Servidor estático local para previsualizar el sitio de Wasi Café.
# Sirve el directorio donde vive este archivo y soporta "clean URLs"
# (/carta -> carta.html, /curso -> curso.html) igual que Cloudflare Pages.
# Uso: ruby serve.rb   (puerto 8080, o PORT=xxxx ruby serve.rb)
require 'webrick'

root = __dir__
port = (ENV['PORT'] || 8080).to_i

server = WEBrick::HTTPServer.new(
  Port: port,
  DocumentRoot: root,
  DirectoryIndex: ['index.html']
)

# Clean URLs: replican el comportamiento de Cloudflare Pages en local.
{ '/carta' => 'carta.html', '/curso' => 'curso.html' }.each do |clean_path, file|
  server.mount_proc(clean_path) do |_req, res|
    res.status = 200
    res['Content-Type'] = 'text/html; charset=utf-8'
    res.body = File.binread(File.join(root, file))
  end
end

trap('INT') { server.shutdown }
puts "Wasi Café -> http://localhost:#{port}/"
server.start
