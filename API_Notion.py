import requests


class ApiNotion:
    def __init__(self):
        try:
            self.Nombre  = str(input("Ingresa el nombre de la tarea: ")).strip()
            self.Descripcion = str(input("Ingresa la descripcion de la tarea: ")).strip()
            self.Estado = str(input("Ingresa el estado de la tarea (Sin empezar, En progreso y Listo): ")).strip()
            self.Fecha_limite = str(input("Ingresa la fecha limite de la tarea (YYYY-MM-DD): ")).strip()
            self.Prioridad = str(input("Ingresa la prioridad de la tarea (Baja, media o alta): ")).strip()
            if not self.Nombre or not (self.Descripcion and self.Fecha_limite and self.Prioridad):
                print("No se pueden agregar los campos en blanco.")
                return

            self.api_key = "TU_API_KEY"
            self.database_id = "TU_DATA_ID"

        except ValueError:
            print("Error de digitacion, vuelve a intentar.")
        except Exception as error:
            print(f"Error en el programa: {error}.")

    def subida_info_tarea(self):
        try:

            url = "https://api.notion.com/v1/pages"

            headers = {
                "Authorization" : f"Bearer {self.api_key}",
                "Content-type" : "application/json",
                "Notion-Version" : "2022-06-28"
            }

            data = {
                "parent" : {"database_id" : self.database_id},
                "properties" : {
                    "Info_tareas" : {"title" : [{"text" : {"content" : self.Nombre}}]},
                    "Descripcion": {"rich_text": [{"text": {"content": self.Descripcion}}]},
                    "Estado" : {"status": {"name" : self.Estado}},
                    "Fecha_limite" : {"rich_text" : [{"text" : {"content" : self.Fecha_limite}}]},
                    "Prioridad" : {"rich_text" : [{"text" : {"content" : self.Prioridad}}]}
                }
            }

            respuesta = requests.post(url, json=data, headers=headers)
            if 200 <= respuesta.status_code < 300:
                print("Tarea subida con exito.")
            else:
                print(f"Error al agregar la tarea: {respuesta.status_code}, {respuesta.json()}.")
        
        except Exception as error:
            print(f"Error en el programa: {error}.")



if __name__ == "__main__":
    tareas = ApiNotion()
    tareas.subida_info_tarea()




