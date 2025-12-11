# Desde la libreria "flask"
# vamos a importar la clase Flask

from flask import Flask

# Desde flask_restful importamos la clase API y la clase
# Resource

from flask_restful import Api, Resource
from rutas import crear_rutas

# Vamos a crear in objeto de tipo Flask

app = Flask(__name__)

# Creamos un objeto de tipo Api y como argumento
# le pasamos el objeto app

# El parametro/argumento que espera recibir es el objeto Flask
api = Api(app)


# La API sera el programa que se comunique con el dispositivo fisico

crear_rutas(api)

# Del objeto app ejecutamos el Metodo run

# 443
# 22
# 21
# 80

app.run(port=8080, debug=True)