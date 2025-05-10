from sistema_ventas.config.config import db

class Proveedor(db.Model):
    __tablename__ = 'proveedores'
    
    rut = db.Column(db.String(12), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    pagina_web = db.Column(db.String(100))
    
    productos = db.relationship('Producto', backref='proveedor', lazy=True)
    
    def to_dict(self):
        return {
            'rut': self.rut,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'pagina_web': self.pagina_web
        }
    