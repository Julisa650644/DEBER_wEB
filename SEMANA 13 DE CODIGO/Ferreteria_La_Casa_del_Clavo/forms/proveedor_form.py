from flask_wtf import FlaskForm
from wtforms import EmailField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp


class ProveedorForm(FlaskForm):
    empresa = StringField(
        "Empresa",
        validators=[DataRequired(message="La empresa es obligatoria."), Length(min=3, max=100)],
    )
    contacto = StringField(
        "Persona de contacto",
        validators=[DataRequired(message="El contacto es obligatorio."), Length(min=3, max=80)],
    )
    telefono = StringField(
        "Teléfono",
        validators=[
            DataRequired(message="El teléfono es obligatorio."),
            Regexp(r"^0\d{8,9}$", message="Ingrese un teléfono válido de 9 o 10 dígitos."),
        ],
    )
    correo = EmailField(
        "Correo electrónico",
        validators=[DataRequired(message="El correo es obligatorio."),
                    Email(message="Ingrese un correo válido."), Length(max=120)],
    )
    producto = StringField(
        "Producto que distribuye",
        validators=[DataRequired(message="Indique el producto que distribuye."), Length(min=3, max=100)],
    )
    estado = SelectField(
        "Estado",
        choices=[("Activo", "Activo"), ("Inactivo", "Inactivo")],
        validators=[DataRequired(message="Seleccione un estado.")],
    )
    submit = SubmitField("Guardar proveedor")
