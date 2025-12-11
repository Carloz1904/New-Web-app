# Las rutas de acceso a cada recurso
from recursos import *

# Tener el objeto api

def crear_rutas(api):
    #quiero
    # 1. El recurso que va a ejecutar - Invocar
    # 2. La direccion de este Recurso
    api.add_resource(HolaMundo, '/hola')

    # La ruta de inicio
    api.add_resource(PantallaInicio, '/')

# Diccionarios
