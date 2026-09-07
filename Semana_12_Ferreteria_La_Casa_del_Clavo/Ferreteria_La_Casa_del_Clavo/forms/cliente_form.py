from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp


class ClienteForm(FlaskForm):
    nombre = StringField(
        "Nombre completo",
        validators=[DataRequired(message="El nombre es obligatorio."), Length(min=3, max=80)],
    )
    telefono = StringField(
        "Teléfono",
        validators=[
            DataRequired(message="El teléfono es obligatorio."),
            Regexp(r"^0\d{9}$", message="Ingrese un teléfono de 10 dígitos que empiece con 0."),
        ],
    )
    correo = EmailField(
        "Correo electrónico",
        validators=[DataRequired(message="El correo es obligatorio."), Email(message="Ingrese un correo válido."), Length(max=120)],
    )
    activo = BooleanField("Cliente activo", default=True)
    submit = SubmitField("Guardar cliente")

