from sistema_ventas.config.config import db

class DetalleVenta(db.Model):
    __tablename__ = 'detalles_ventas'
    
    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_venta = db.Column(db.Float, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'venta_id': self.venta_id,
            'producto_id': self.producto_id,
            'cantidad': self.cantidad,
            'precio_venta': self.precio_venta,
            'subtotal': self.subtotal
        }
    