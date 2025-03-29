import requests
from notion_client import Client

class ApiNotion:
    def __init__(self):
        try:
            self.nombre_tarea = str(input("Ingresa el nombre de la tarea: ")).strip()
            self.descripcion_tarea = str(input("Ingresa la descripcion de la tareaç: ")).strip()
            self.estado_tarea = str(input("Ingresa el estado de la tarea (Pendiente, en progreso y finalizado): ")).strip()
            self.fecha_limite_tarea = str(input("Ingresa la fecha limite de la tarea: ")).strip()
            self.prioridad_tarea = str(input("Ingresa la prioridad de la tarea (Baja, media o alta): ")).strip()
            if not self.nombre_tarea or not (self.descripcion_tarea and self.fecha_limite_tarea and self.prioridad_tarea):
                print("No se pueden agregar los campos en blanco.")
                return

            self.notion_key = "NOTION_KEY"
            self.notion = Client(auth = self.notion_key)
            self.database_id = "ID_DATABSE"

        except ValueError:
            print("Error de digitacion, vuelve a intentar.")
        except Exception as error:
            print(f"Error en el programa: {error}.")

    def subida_nombre_tarea(self):

        url = "https://api.notion.com/v1/pages"

        headers = {
            "Authorization" : f"Bearer {self.notion_key}",
            "Content-type" : "application/json",
            "Notion-Version" : "2022-06-28"
        }

        data = {
            "parent" : {"database_id" : self.database_id},
            "properties" : {
                "nombre" : {"title" : [{"text" : {"content" : self.nombre_tarea}}]}
            }
        }

        respuesta = requests.post(url, json=data, headers=headers)
        if 200 <= respuesta.status_code < 300:
            print("Tarea subida con exito.")
        else:
            print(f"Error al agregar la tarea: {respuesta.status_code}, {respuesta.text}.")


