from sistema_ventas.config.config import db

class Producto(db.Model):
    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    proveedor_rut = db.Column(db.String(12), db.ForeignKey('proveedores.rut'), nullable=False)
    
    detalles_venta = db.relationship('DetalleVenta', backref='producto', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'stock': self.stock,
            'categoria_id': self.categoria_id,
            'proveedor_rut': self.proveedor_rut
        }
    