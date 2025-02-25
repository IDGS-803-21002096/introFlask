from flask import Flask, render_template, request
from flask import g
from flask_wtf.csrf import CSRFProtect
from flask import flash
import forms

app = Flask(__name__) 
app.secret_key="Esta es la clave secreta"
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.nombre = "Mario"
    print(' Before request 1')

@app.after_request
def after_request(response):
    print(' After request 3')
    return response

@app.route('/')
def index():
    grupo="IDGS803"
    lista = ["Juan", "Pedro", "Mario"]
    print('Index 2')
    print('Hola {}', format(g.nombre))
    return render_template("index.html", grupo=grupo, lista=lista) #Abre el archivo html con el render

@app.route('/Alumnos', methods=["GET","POST"])
def alumnos():
    mat=''
    nom=''
    edad=''
    correo=''
    ape=''
    alumno_clase = forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clase.validate():
        mat=alumno_clase.matricula.data
        nom=alumno_clase.nombre.data
        ape=alumno_clase.apellidos.data
        edad=alumno_clase.edad.data
        correo=alumno_clase.correo.data
        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("Alumnos.html", form=alumno_clase, mat=mat, nom=nom, ape=ape, edad=edad, correo=correo)

@app.route('/OperasBas', methods=["GET","POST"])
def operas():
    resultado = None
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        resultado = "La suma de {} + {} es {}".format(num1, num2,int(num1)+int(num2))
    return render_template("OperasBas.html", resultado=resultado)

@app.route('/resultado', methods=["GET","POST"])
def resultado():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La suma de {} + {} es {}".format(num1, num2,int(num1)+int(num2))

@app.route('/cinepolis', methods=["GET", "POST"])
def cinepolis():
    
    total_pagar = 0
    resultado = 0
    nombre = ""
    compradores = ""
    tarjeta = ""
    boletos = ""

    if request.method == "POST":
        
        #Traer los dato
        nombre = request.form.get("nombre")
        compradores = int(request.form.get("compradores"))
        tarjeta = request.form.get("tarjeta")
        boletos = int(request.form.get("boletos"))
        
        #Validar boletos
        maxboletos = compradores * 7
        if boletos > maxboletos:
            resultado = f"No puedes comprar más de {maxboletos} boletos."
        else:
            precio_boleto = 12
            total_pagar = boletos * precio_boleto

            #Aplicar descuentos
            if boletos > 5:
                descuento = total_pagar * 0.15
                total_pagar -= descuento
            elif 3 <= boletos <= 5:
                descuento = total_pagar * 0.10
                total_pagar -= descuento

            # Validación de tarjeta
            if tarjeta == "Si":
                descuento_tarjeta = total_pagar * 0.10
                total_pagar -= descuento_tarjeta
            
            resultado = f"{ nombre } debe pagar la cantidad de $ { total_pagar } por adquirir { boletos } boletos"

    return render_template("cinepolis.html", resultado=resultado)

@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route('/ejemplo2')
def ejemplo2():
    return render_template("ejemplo2.html")

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

@app.route('/form1')
def form1():
    return '''
        <form>
        <label>Nombre: </label>
        <input type="text" name="nombre" placeholder="nombre">
        </br>
        <form>
        <label>Nombre: </label>
        <input type="text" name="nombre" placeholder="nombre">
        </br>
        </form>
    '''

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True, port=3000)