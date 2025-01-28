from flask import Flask

app = Flask(__name__) #Se crea la aplicacion como tal

@app.route('/')
def index():
    return "Hola Mundo!!!"

@app.route('/hola')
def hola():
    return "Hola!!"

@app.route('/user/<string:user>')
def user(user):
    return f"Hola {user}!!!"

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)

@app.route('/user/<string:user>/<int:id>')
def username(user,id):
    return f"Nombre: {user} ID: {id}!!!"

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1,n2):
    return "La suma es: {}!!!".format(n1+n2)

@app.route('/default')
@app.route('/default/<string:nom>')
def func(nom = 'pedro'):
    return "El nombre de nom es "+nom

if __name__ == '__main__':
    app.run(debug=True, port=3000)