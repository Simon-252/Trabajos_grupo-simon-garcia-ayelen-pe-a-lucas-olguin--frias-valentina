from flask import Blueprint, jsonify
from sistema_ventas.config.config import db  
from sistema_ventas.models.venta import Venta
from sistema_ventas.models.detalle_venta import DetalleVenta

ventas_bp = Blueprint('ventas', __name__)

@ventas_bp.route('/', methods=['GET'])
def get_ventas():
    try:
        ventas = Venta.query.options(db.joinedload(Venta.cliente)).all()
        resultado = []
        for v in ventas:
            resultado.append({
                'id': v.id,
                'fecha': v.fecha.strftime('%Y-%m-%d %H:%M:%S'),
                'cliente': {
                    'rut': v.cliente.rut,
                    'nombre': v.cliente.nombre
                },
                'total': v.monto_final,
                'detalles': [
                    {
                        'producto_id': d.producto_id,
                        'cantidad': d.cantidad,
                        'precio_unitario': d.precio_venta,
                        'subtotal': d.subtotal
                    } for d in v.detalles
                ]
            })
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)}), 500