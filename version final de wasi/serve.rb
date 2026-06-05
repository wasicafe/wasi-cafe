#!/usr/bin/env ruby
# Servidor estático local para previsualizar el sitio de Wasi Café.
# Sirve el directorio donde vive este archivo. Uso: ruby serve.rb
require 'webrick'

root = __dir__
port = (ENV['PORT'] || 8080).to_i

server = WEBrick::HTTPServer.new(
  Port: port,
  DocumentRoot: root,
  DirectoryIndex: ['index.html']
)
trap('INT') { server.shutdown }
puts "Wasi Café -> http://localhost:#{port}/"
server.start
