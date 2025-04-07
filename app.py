from flask import Flask, render_template, redirect, url_for, flash
from forms import ContactForm

# Configuración de la aplicación Flask
app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Clave secreta para gestionar sesiones

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de la Prótesis de Mano
@app.route('/servicio-mano')
def servicio_mano():
    return render_template('servicio_mano.html')

# Ruta para la página de la Prótesis de Pie
@app.route('/servicio-pie')
def servicio_pie():
    return render_template('servicio_pie.html')

# Ruta para la página de Rehabilitación y Adaptación
@app.route('/servicio-recuperacion')
def servicio_recuperacion():
    return render_template('servicio_recuperacion.html')

# Ruta para la página de Consulta y Asesoría Técnica
@app.route('/servicio-consulta')
def servicio_consulta():
    return render_template('servicio_consulta.html')

# Ruta sobre "Quiénes somos"
@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

# Ruta para ver los servicios
@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

# Ruta para ver las noticias
@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

# Ruta para el formulario de contacto
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactForm()  # Crear instancia del formulario
    if form.validate_on_submit():  # Si el formulario es válido
        # Obtener los datos ingresados
        nombre = form.nombre.data
        correo = form.correo.data
        telefono = form.telefono.data
        asunto = form.asunto.data
        mensaje = form.mensaje.data
        
        # Mostrar mensaje de éxito y redirigir a la página de reporte
        flash('Mensaje enviado con éxito.')
        return render_template('reporte.html', nombre=nombre, correo=correo, telefono=telefono, asunto=asunto, mensaje=mensaje)
       
    # Si el formulario no se envió o es inválido, vuelve a mostrar el formulario
    return render_template('contacto.html', form=form)

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)


