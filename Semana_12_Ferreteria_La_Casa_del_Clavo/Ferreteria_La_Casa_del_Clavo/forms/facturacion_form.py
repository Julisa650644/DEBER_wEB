from flask_wtf import FlaskForm
from wtforms import DateField, DecimalField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class FacturacionForm(FlaskForm):
    numero = StringField(
        "Número de factura",
        validators=[DataRequired(message="El número es obligatorio."), Length(min=3, max=15)],
    )
    cliente = SelectField(
        "Cliente",
        choices=[],
        validators=[DataRequired(message="Seleccione un cliente.")],
    )
    fecha = DateField(
        "Fecha",
        format="%Y-%m-%d",
        validators=[DataRequired(message="La fecha es obligatoria.")],
    )
    total = DecimalField(
        "Total",
        places=2,
        validators=[DataRequired(message="El total es obligatorio."), NumberRange(min=0.01, message="El total debe ser mayor que cero.")],
    )
    estado = SelectField(
        "Estado",
        choices=[("Pendiente", "Pendiente"), ("Pagada", "Pagada")],
        validators=[DataRequired(message="Seleccione un estado.")],
    )
    submit = SubmitField("Guardar factura")

