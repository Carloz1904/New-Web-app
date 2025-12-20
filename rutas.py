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

# Le damos una ruta al inicio de sesion
    api.add_resource(login, '/login')

# Le damos una ruta a la creacion de cuenta
    api.add_resource(sign_up, '/signup')

# Diccionarios
