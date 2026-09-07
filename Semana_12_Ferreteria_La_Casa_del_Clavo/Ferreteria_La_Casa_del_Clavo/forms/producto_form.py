from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange


class ProductoForm(FlaskForm):
    codigo = StringField(
        "Código",
        validators=[DataRequired(message="El código es obligatorio."), Length(min=2, max=10)],
    )
    nombre = StringField(
        "Nombre del producto",
        validators=[DataRequired(message="El nombre es obligatorio."), Length(min=3, max=80)],
    )
    categoria = SelectField(
        "Categoría",
        choices=[
            ("", "Seleccione una categoría"),
            ("Herramientas", "Herramientas"),
            ("Fijaciones", "Fijaciones"),
            ("Materiales", "Materiales"),
            ("Electricidad", "Electricidad"),
            ("Plomería", "Plomería"),
        ],
        validators=[DataRequired(message="Seleccione una categoría.")],
    )
    precio = DecimalField(
        "Precio",
        places=2,
        validators=[DataRequired(message="El precio es obligatorio."), NumberRange(min=0.01, message="El precio debe ser mayor que cero.")],
    )
    stock = IntegerField(
        "Stock",
        validators=[InputRequired(message="El stock es obligatorio."), NumberRange(min=0, message="El stock no puede ser negativo.")],
    )
    descripcion = TextAreaField(
        "Descripción",
        validators=[DataRequired(message="La descripción es obligatoria."), Length(min=5, max=200)],
    )
    submit = SubmitField("Guardar producto")
