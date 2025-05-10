from sistema_ventas.config.config import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    rut = db.Column(db.String(12), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    calle = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    comuna = db.Column(db.String(50), nullable=False)
    ciudad = db.Column(db.String(50), nullable=False)
    
    telefonos = db.relationship('TelefonoCliente', backref='cliente', cascade='all, delete-orphan', lazy=True)
    ventas = db.relationship('Venta', backref='cliente', lazy=True)
    
    def to_dict(self):
        return {
            'rut': self.rut,
            'nombre': self.nombre,
            'direccion': {
                'calle': self.calle,
                'numero': self.numero,
                'comuna': self.comuna,
                'ciudad': self.ciudad
            },
            'telefonos': [tel.numero for tel in self.telefonos]
        }
    