from flask import Blueprint, jsonify, request
from sistema_ventas.models.cliente import Cliente
from sistema_ventas.models.telefono_cliente import TelefonoCliente
from sistema_ventas.config.config import db

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([c.to_dict() for c in clientes])

@clientes_bp.route('/', methods=['POST'])
def crear_cliente():
    data = request.get_json()
    
    nuevo_cliente = Cliente(
        rut=data['rut'],
        nombre=data['nombre'],
        calle=data['direccion']['calle'],
        numero=data['direccion']['numero'],
        comuna=data['direccion']['comuna'],
        ciudad=data['direccion']['ciudad']
    )
    
    db.session.add(nuevo_cliente)
    
    for telefono in data['telefonos']:
        db.session.add(TelefonoCliente(
            numero=telefono,
            cliente_rut=data['rut']
        ))
    
    db.session.commit()
    return jsonify(nuevo_cliente.to_dict()), 201

@clientes_bp.route('/<rut>', methods=['GET'])
def get_cliente(rut):
    cliente = Cliente.query.get_or_404(rut)
    return jsonify(cliente.to_dict())
