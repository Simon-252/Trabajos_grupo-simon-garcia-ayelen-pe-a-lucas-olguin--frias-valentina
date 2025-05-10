import os
import sys
import json
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)


from sistema_ventas.app import create_app
from sistema_ventas.config.config import db

def load_sample_data():
    app = create_app()
    
    with app.app_context():
        print("Reiniciando base de datos...")
        db.drop_all()
        print("Creando tablas...")
        db.create_all()

        try:

            from sistema_ventas.models import (
                Proveedor, Cliente, TelefonoCliente,
                Categoria, Producto, Venta, DetalleVenta
            )

            print("Cargando categorías...")
            with open(os.path.join(BASE_DIR, 'sistema_ventas', 'data', 'categorias.json'), encoding='utf-8') as f:
                categorias = json.load(f)
                for cat in categorias:
                    db.session.add(Categoria(**cat))
                db.session.commit()
                print(f"{len(categorias)} categorías cargadas")


            print("Cargando proveedores...")
            with open(os.path.join(BASE_DIR, 'sistema_ventas', 'data', 'proveedores.json'), encoding='utf-8') as f:
                proveedores = json.load(f)
                for prov in proveedores:
                    db.session.add(Proveedor(**prov))
                db.session.commit()
                print(f"{len(proveedores)} proveedores cargados")


            print("Cargando productos...")
            with open(os.path.join(BASE_DIR, 'sistema_ventas', 'data', 'productos.json'), encoding='utf-8') as f:
                productos = json.load(f)
                for prod in productos:
                    db.session.add(Producto(**prod))
                db.session.commit()
                print(f"{len(productos)} productos cargados")


            print("Cargando clientes...")
            with open(os.path.join(BASE_DIR, 'sistema_ventas', 'data', 'clientes.json'), encoding='utf-8') as f:
                clientes = json.load(f)
                for cli in clientes:
                    telefonos = cli.pop('telefonos', [])
                    cliente = Cliente(**cli)
                    db.session.add(cliente)
                    for tel in telefonos:
                        db.session.add(TelefonoCliente(numero=tel, cliente_rut=cli['rut']))
                db.session.commit()
                print(f"{len(clientes)} clientes cargados")

            if os.path.exists(os.path.join(BASE_DIR, 'sistema_ventas', 'data', 'ventas.json')):
                print("Cargando ventas...")
                with open(os.path.join(BASE_DIR, 'sistema_ventas', 'data', 'ventas.json'), encoding='utf-8') as f:
                    ventas = json.load(f)
                    for venta_data in ventas:
                        detalles = venta_data.pop('detalles', [])
                        venta_data['fecha'] = datetime.fromisoformat(venta_data['fecha'])
                        
                        venta = Venta(**venta_data)
                        db.session.add(venta)
                        db.session.flush() 
                        
                        for det in detalles:
                            db.session.add(DetalleVenta(
                                venta_id=venta.id,
                                **det
                            ))
                    db.session.commit()
                    print(f"{len(ventas)} ventas cargadas")

            print("¡Base de datos inicializada exitosamente!")

        except Exception as e:
            db.session.rollback()
            print(f"Error crítico: {str(e)}")
            raise

if __name__ == '__main__':

    db_path = os.path.join(BASE_DIR, 'instance', 'sistema_ventas.db')
    if os.path.exists(db_path):
        print(f"Eliminando base de datos existente: {db_path}")
        os.remove(db_path)
    
    load_sample_data()