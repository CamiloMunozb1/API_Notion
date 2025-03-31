import requests  # Importamos la librería requests para hacer peticiones HTTP.


class ApiNotion:
    def __init__(self):
        try:
            # Solicitamos al usuario que ingrese los detalles de la tarea y eliminamos espacios extra.
            self.Nombre = str(input("Ingresa el nombre de la tarea: ")).strip()
            self.Descripcion = str(input("Ingresa la descripcion de la tarea: ")).strip()
            self.Estado = str(input("Ingresa el estado de la tarea (Sin empezar, En progreso y Listo): ")).strip()
            self.Fecha_limite = str(input("Ingresa la fecha limite de la tarea (YYYY-MM-DD): ")).strip()
            self.Prioridad = str(input("Ingresa la prioridad de la tarea (Baja, media o alta): ")).strip()

            # Validamos que los campos obligatorios no estén vacíos.
            if not self.Nombre or not (self.Descripcion and self.Fecha_limite and self.Prioridad):
                print("No se pueden agregar los campos en blanco.")
                return  # Salimos del constructor si faltan datos.

            # Claves necesarias para conectar con la API de Notion.
            self.api_key = "TU_API_KEK"  # Token de autenticación (debe mantenerse seguro).
            self.database_id = "TU_DATABASE_ID"  # ID de la base de datos en Notion.

        except ValueError:
            print("Error de digitación, vuelve a intentar.")
        except Exception as error:
            print(f"Error en el programa: {error}.")  # Manejamos cualquier otro error inesperado.

    def subida_info_tarea(self):
        """Envía la información de la tarea a Notion utilizando la API."""
        try:
            url = "https://api.notion.com/v1/pages"  # URL de la API de Notion para crear una nueva página.

            headers = {
                "Authorization": f"Bearer {self.api_key}",  # Autenticación con el token de API.
                "Content-type": "application/json",  # Especificamos el tipo de contenido.
                "Notion-Version": "2022-06-28"  # Versión de la API de Notion.
            }

            # Estructura de datos que se enviará a Notion con los detalles de la tarea.
            data = {
                "parent": {"database_id": self.database_id},  # Definimos la base de datos en Notion.
                "properties": {
                    "Info_tareas": {"title": [{"text": {"content": self.Nombre}}]},  # Nombre de la tarea.
                    "Descripcion": {"rich_text": [{"text": {"content": self.Descripcion}}]},  # Descripción.
                    "Estado": {"status": {"name": self.Estado}},  # Estado de la tarea.
                    "Fecha_limite": {"rich_text": [{"text": {"content": self.Fecha_limite}}]},  # Fecha límite.
                    "Prioridad": {"rich_text": [{"text": {"content": self.Prioridad}}]}  # Nivel de prioridad.
                }
            }

            # Enviamos la petición POST a Notion con los datos.
            respuesta = requests.post(url, json=data, headers=headers)

            # Verificamos si la respuesta es exitosa (códigos 200-299).
            if 200 <= respuesta.status_code < 300:
                print("Tarea subida con éxito.")
            else:
                # Si hay un error, mostramos el código de estado y el mensaje de respuesta.
                print(f"Error al agregar la tarea: {respuesta.status_code}, {respuesta.json()}.")

        except Exception as error:
            print(f"Error en el programa: {error}.")  # Manejamos cualquier error inesperado.


# Ejecutamos el código solo si el script se ejecuta directamente.
if __name__ == "__main__":
    tareas = ApiNotion()  # Creamos una instancia de la clase.
    tareas.subida_info_tarea()  # Subimos la información de la tarea a Notion.




