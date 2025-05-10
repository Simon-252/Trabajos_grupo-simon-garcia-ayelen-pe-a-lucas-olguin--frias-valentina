import os
import sys
from flask import Flask


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

def create_app():
    app = Flask(__name__)
    

    app.config.from_object('sistema_ventas.config.config.Config')
    

    from sistema_ventas.config.config import db
    db.init_app(app)
    

    from sistema_ventas.routes.proveedores import proveedores_bp
    from sistema_ventas.routes.clientes import clientes_bp
    from sistema_ventas.routes.productos import productos_bp
    from sistema_ventas.routes.ventas import ventas_bp
    
    app.register_blueprint(proveedores_bp, url_prefix='/api/proveedores')
    app.register_blueprint(clientes_bp, url_prefix='/api/clientes')
    app.register_blueprint(productos_bp, url_prefix='/api/productos')
    app.register_blueprint(ventas_bp, url_prefix='/api/ventas')
    

    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
