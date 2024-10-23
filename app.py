from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de productos
productos = [
    {"nombre": "Coliflor", "categoria": "Verdura", "cantidad": 10, "fecha_adquisicion": "2022-01-01"},
    {"nombre": "Lulo", "categoria": "Fruta", "cantidad": 5, "fecha_adquisicion": "2022-02-01"}
]

# Obtener todos los productos
@app.route('/productos', methods=['GET'])
def get_productos():
    return jsonify(productos)

# Obtener un producto por nombre
@app.route('/productos/<nombre>', methods=['GET'])
def get_producto(nombre):
    for producto in productos:
        if producto['nombre'] == nombre:
            return jsonify(producto)
    return jsonify({"mensaje": "Producto no encontrado"})

# Crear un nuevo producto
@app.route('/productos', methods=['POST'])
def create_producto():
    nuevo_producto = {
        "nombre": request.json['nombre'],
        "categoria": request.json['categoria'],
        "cantidad": request.json['cantidad'],
        "fecha_adquisicion": request.json['fecha_adquisicion']
    }
    productos.append(nuevo_producto)
    return jsonify(nuevo_producto)

# Actualizar un producto
@app.route('/productos/<nombre>', methods=['PUT'])
def update_producto(nombre):
    for producto in productos:
        if producto['nombre'] == nombre:
            producto['nombre'] = request.json.get('nombre', producto['nombre'])
            producto['categoria'] = request.json.get('categoria', producto['categoria'])
            producto['cantidad'] = request.json.get('cantidad', producto['cantidad'])
            producto['fecha_adquisicion'] = request.json.get('fecha_adquisicion', producto['fecha_adquisicion'])
            return jsonify(producto)
    return jsonify({"mensaje": "Producto no encontrado"})

# Eliminar un producto
@app.route('/productos/<nombre>', methods=['DELETE'])
def delete_producto(nombre):
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            return jsonify({"mensaje": "Producto eliminado"})
    return jsonify({"mensaje": "Producto no encontrado"})

if __name__ == '__main__':
    app.run(debug=True)