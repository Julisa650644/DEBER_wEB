from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class ProveedorForm(FlaskForm):
    identificador = StringField(
        "ID del proveedor",
        validators=[DataRequired(message="El ID es obligatorio."), Length(min=3, max=10)],
    )
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

