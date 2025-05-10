import requests

BASE_URL = "http://localhost:5000/api"

def crear_producto():
    url = f"{BASE_URL}/productos"
    datos = {
        "nombre": "Teclado Mecánico",
        "precio": 25000,
        "stock": 15,
        "categoria_id": 1,
        "proveedor_rut": "12345678-9"
    }
    
    response = requests.post(url, json=datos)
    
    if response.status_code == 201:
        print("Producto creado:")
        print(response.json())
    else:
        print(f"Error {response.status_code}:")
        print(response.text)


def listar_productos():
    response = requests.get(f"{BASE_URL}/productos")
    print("Productos existentes:")
    for producto in response.json():
        print(f"- {producto['nombre']} (${producto['precio']})")

if __name__ == "__main__":
    crear_producto()
    listar_productos()