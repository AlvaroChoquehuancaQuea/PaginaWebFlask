from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    """
    Formulario de contacto para enviar un mensaje.
    """
    # Nombre del usuario (requerido)
    nombre = StringField('Nombre', validators=[DataRequired()])

    # Correo electrónico del usuario (requerido y validado)
    correo = StringField('Correo Electrónico', validators=[DataRequired(), Email()])

    # Teléfono del usuario (opcional)
    telefono = StringField('Teléfono')

    # Asunto del mensaje (requerido)
    asunto = SelectField('Asunto', choices=[
        ('consulta', 'Consulta'),
        ('soporte', 'Soporte Técnico'),
        ('sugerencia', 'Sugerencia'),
        ('otro', 'Otro')
    ], validators=[DataRequired()])

    # Mensaje del usuario (requerido)
    mensaje = TextAreaField('Mensaje', validators=[DataRequired()])

    # Botón de envío
    submit = SubmitField('Enviar Mensaje')
