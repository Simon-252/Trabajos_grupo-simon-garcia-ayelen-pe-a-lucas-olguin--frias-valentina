from sistema_ventas.config.config import db

class TelefonoCliente(db.Model):
    __tablename__ = 'telefonos_clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), nullable=False, unique=True)
    cliente_rut = db.Column(db.String(12), db.ForeignKey('clientes.rut', ondelete='CASCADE'), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'numero': self.numero,
            'cliente_rut': self.cliente_rut
        }
    