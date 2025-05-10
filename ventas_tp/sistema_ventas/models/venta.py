from datetime import datetime
from sistema_ventas.config.config import db

class Venta(db.Model):
    __tablename__ = 'ventas'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    cliente_rut = db.Column(db.String(12), db.ForeignKey('clientes.rut'), nullable=False)
    descuento = db.Column(db.Float, default=0.0)
    monto_final = db.Column(db.Float, nullable=False)
    
    detalles = db.relationship('DetalleVenta', backref='venta', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'fecha': self.fecha.isoformat(),
            'cliente_rut': self.cliente_rut,
            'descuento': self.descuento,
            'monto_final': self.monto_final,
            'detalles': [det.to_dict() for det in self.detalles]
        }
    