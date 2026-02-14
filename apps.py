from flask import Flask

app = Flask(__name__)

# 1. Ruta Principal (Home)
# Muestra el propósito del negocio como se solicita
@app.route('/')
def home():
    return '''
    <h1>Sistema de Gestión LOGICON S.A.</h1>
    <p>Bienvenido al Centro de Control de Abastos y Logística Continental.</p>
    <hr>
    <p>Estado del Sistema: <b>Operacional - Febrero 2026</b></p>
    '''

# 2. Ruta Dinámica: Consulta de Inventario
# Ejemplo: http://127.0.0.1:5000/item/L001
@app.route('/item/<codigo>')
def consultar_item(codigo):
    # En el futuro, aquí haremos una consulta SELECT a la tabla PRODUCTO
    return f'📦 <b>Consulta de Inventario:</b> El ítem con código <b>{codigo}</b> se encuentra registrado en bodega.'

# 3. Ruta Dinámica: Estado de Envío
# Ejemplo: http://127.0.0.1:5000/envio/901
@app.route('/envio/<id_envio>')
def estado_envio(id_envio):
    # Relacionado con la tabla ENVIO y VEHICULO
    return f'🚚 <b>Logística:</b> El envío No. <b>{id_envio}</b> está asignado al transporte y en ruta a su destino.'

if __name__ == '__main__':

    app.run(debug=True)
