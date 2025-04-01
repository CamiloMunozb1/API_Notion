# Gestor de Tareas con Notion API

Este proyecto permite gestionar tareas mediante la API de Notion, facilitando la creación de tareas con atributos como nombre, descripción, estado, fecha límite y prioridad.

## Características
- Permite ingresar tareas con datos específicos.
- Envía la información a una base de datos de Notion.
- Usa la API de Notion para gestionar los datos de manera eficiente.

## Requisitos
- Python 3.x
- Biblioteca `requests`
- Una cuenta en [Notion](https://www.notion.so/)
- Una clave de API de Notion
- Un ID de base de datos en Notion

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   cd TU_REPOSITORIO
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install requests
   ```
3. Configura las variables de la API para ingresar tu base de datos:
   ```
   NOTION_API_KEY=tu_api_key
   NOTION_DATABASE_ID=tu_database_id
   ```

## Uso
1. Ejecuta el script:
   ```bash
   python main.py
   ```
2. Ingresa los datos de la tarea cuando se te solicite.
3. La tarea se añadirá a la base de datos de Notion.

## Estructura del Proyecto
```
/
├── main.py  # Código principal del gestor de tareas
├── README.md  # Documentación del proyecto
```

## Notas
- Asegúrate de no compartir tu clave de API públicamente.
- Puedes modificar el código para agregar más funcionalidades según tus necesidades.

## Autor
Desarrollado por Juan Camilo Muñoz.

## Licencia
Este proyecto está bajo la licencia MIT.

