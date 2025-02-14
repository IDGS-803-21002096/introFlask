from wtforms import form
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, Regexp
from wtforms import StringField, EmailField PasswordField, SubmitField, IntegerField, SelectField, DecimalField

class UserForm(Form):
    matricula=StringField("Matricula")
    edad=IntegerField("Edad")
    nombre=StringField("Nombre")
    apelidos=StringField("Apellidos")
    correo=EmailField("Correo")