from flask import Blueprint, jsonify, request
from sistema_ventas.models.proveedor import Proveedor
from sistema_ventas.config.config import db


proveedores_bp = Blueprint('proveedores', __name__)

@proveedores_bp.route('/', methods=['GET'])
def get_proveedores():
    proveedores = Proveedor.query.all()
    return jsonify([p.to_dict() for p in proveedores])

@proveedores_bp.route('/', methods=['POST'])
def crear_proveedor():
    data = request.get_json()
    
    nuevo_proveedor = Proveedor(
        rut=data['rut'],
        nombre=data['nombre'],
        direccion=data['direccion'],
        telefono=data['telefono'],
        pagina_web=data.get('pagina_web')
    )
    
    db.session.add(nuevo_proveedor)
    db.session.commit()
    return jsonify(nuevo_proveedor.to_dict()), 201

@proveedores_bp.route('/<rut>', methods=['GET'])
def get_proveedor(rut):
    proveedor = Proveedor.query.get_or_404(rut)
    return jsonify(proveedor.to_dict())
