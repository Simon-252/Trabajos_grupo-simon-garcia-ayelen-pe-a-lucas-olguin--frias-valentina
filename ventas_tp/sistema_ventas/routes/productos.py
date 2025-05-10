from flask import Blueprint, jsonify, request
from sistema_ventas.models.producto import Producto
from sistema_ventas.config.config import db

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    return jsonify([p.to_dict() for p in productos])

@productos_bp.route('/', methods=['POST'])
def crear_producto():
    data = request.get_json()
    
    nuevo_producto = Producto(
        nombre=data['nombre'],
        precio=data['precio'],
        stock=data['stock'],
        categoria_id=data['categoria_id'],
        proveedor_rut=data['proveedor_rut']
    )
    
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify(nuevo_producto.to_dict()), 201

@productos_bp.route('/<int:id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get_or_404(id)
    return jsonify(producto.to_dict())
