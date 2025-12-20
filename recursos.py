from flask_restful import Resource

from flask import make_response, render_template
# Los recursos que mi servidor tendra disponible



# VAmos a crear Recursos - Para nosotros poder crear recursos
# lo haremos a traves de clases y objetos
class HolaMundo(Resource):
    # Los recursos van a poder ejecutar dos acciones -> metodos
    def get(self):
        return {'hola': 'mundo'}

# Sera un recurso
class PantallaInicio(Resource):
    def get(self):
        #Renderizamos el contenido del archivo html
        contenido = render_template('index.html')

        # Retornar el contenido renderizado en una respuesta
        return make_response(contenido)

class login(Resource):
    def get(self):

        contenido = render_template('login.html')

        return make_response(contenido)

class sign_up(Resource):
    def get(self):
        contenido = render_template('sign_up.html')
        return make_response(contenido)