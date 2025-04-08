# API REST para Obtener Eventos desde MySQL (Flask)

Esta es una sencilla API REST desarrollada con Flask (Python) que se conecta a una base de datos MySQL y expone un endpoint para obtener una lista de eventos en formato JSON.

## Funcionalidades Principales

* **Endpoint `/` (GET):** Al realizar una petición GET a la raíz de la aplicación, se consulta una tabla llamada `Eventos` en la base de datos MySQL configurada y se devuelve un array de objetos JSON, donde cada objeto representa un evento con los siguientes campos:
    * `id_evento`: Identificador único del evento.
    * `nombre_evento`: Nombre del evento.
    * `descripcion`: Descripción del evento.
    * `lugar`: Lugar donde se llevará a cabo el evento.
    * `creador`: Persona o entidad creadora del evento.
    * `duracion`: Duración del evento (se devuelve como string).
* **Manejo de Errores:** En caso de fallas al conectar con la base de datos o al ejecutar la consulta, la API devuelve una respuesta JSON con un mensaje de error y un código de estado HTTP 500 (Error interno del servidor).

## Cómo Utilizar

1.  **Clonar el Repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <nombre_del_repositorio>
    ```

2.  **Crear un Entorno Virtual (Recomendado):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate  # En Windows
    ```

3.  **Instalar las Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Si no existe un archivo `requirements.txt`, instala las dependencias necesarias con `pip install Flask mysql-connector-python`)*

4.  **Configurar la Base de Datos:**
    * Edita el archivo principal de la aplicación (`app.py`) y actualiza la sección `db_config` con los detalles de tu base de datos MySQL:
        ```python
        db_config = {
            "host": "localhost",  # Cambia a la dirección de tu servidor MySQL si es diferente
            "user": "usuarioBBDD",  # Reemplaza con tu nombre de usuario de MySQL
            "password": "password",  # Reemplaza con la contraseña de tu usuario de MySQL
            "database": "nameBBDD"  # Reemplaza con el nombre de tu base de datos
        }
        ```
    * Asegúrate de tener una base de datos llamada `nameBBDD` (o el nombre que hayas configurado) y una tabla llamada `Eventos` con las columnas `id_evento`, `nombre_evento`, `descripcion`, `lugar`, `creador` y `duracion`.

5.  **Ejecutar la Aplicación:**
    ```bash
    python app.py
    ```

6.  **Acceder a la API:** Abre tu cliente HTTP favorito (como `curl`, Postman, Insomnia, o un navegador web) y realiza una petición GET a la dirección `http://127.0.0.1:5000/` (o la dirección y puerto donde se esté ejecutando tu aplicación).

7.  **Ver los Resultados:** La respuesta será un array JSON que contiene la información de todos los eventos encontrados en la tabla `Eventos` de tu base de datos MySQL.

## Configuración

La configuración principal se realiza directamente en el diccionario `db_config` dentro del archivo `app.py`. Asegúrate de proporcionar los valores correctos para conectar con tu instancia de MySQL.
