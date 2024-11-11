from typing import Any, Dict

# Definir Servicios (Lógica de Negocio)
class UserService:
    def get_user(self, user_id: int) -> str:
        return f"Datos del usuario con ID {user_id}"

class ProductService:
    def get_product(self, product_id: int) -> str:
        return f"Detalles del producto con ID {product_id}"

# Definir el Application Controller
class ApplicationController:
    def __init__(self):
        # El controlador tiene referencias a los servicios
        self.services = {
            "user": UserService(),
            "product": ProductService()
        }

    def handle_request(self, request: Dict[str, Any]) -> str:
        """
        Procesa la solicitud entrante y la dirige al servicio adecuado.
        """
        service_type = request.get("type")
        action = request.get("action")
        
        if service_type == "user" and action == "get_user":
            user_id = request.get("user_id")
            return self.services["user"].get_user(user_id)
        elif service_type == "product" and action == "get_product":
            product_id = request.get("product_id")
            return self.services["product"].get_product(product_id)
        else:
            return "Error: Solicitud no válida"

# Definir un cliente de ejemplo que usa el ApplicationController
def client_code():
    controller = ApplicationController()
    
    # Simular una solicitud de usuario
    user_request = {
        "type": "user",
        "action": "get_user",
        "user_id": 123
    }
    print(controller.handle_request(user_request))  # Salida: Datos del usuario con ID 123

    # Simular una solicitud de producto
    product_request = {
        "type": "product",
        "action": "get_product",
        "product_id": 456
    }
    print(controller.handle_request(product_request))  # Salida: Detalles del producto con ID 456

    # Simular una solicitud no válida
    invalid_request = {
        "type": "unknown",
        "action": "invalid_action"
    }
    print(controller.handle_request(invalid_request))  # Salida: Error: Solicitud no válida

# Ejecutar el código del cliente
client_code()
