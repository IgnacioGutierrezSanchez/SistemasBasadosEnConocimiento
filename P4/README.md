# PRÁCTICA 4: Asistentes basados en lenguaje


Este proyecto implementa un asistente virtual académico que utiliza un modelo de lenguaje basado en **Ollama** para responder preguntas relacionadas con un conjunto de conocimientos previamente cargados. El sistema soporta dos modos de operación principales: **RAG (Retrieve and Generate)** y **Chain of Thought (CoT)**, el cual simula un proceso de razonamiento paso a paso antes de responder.

## 🗂️ Estructura del Proyecto
La estructura del proyecto es la siguiente:

- knowledge_base/
   - professors: Parte de la base de conocimiento con la información de los docentes.
   - students: Parte de la base de conocimiento con la información de los alumnos.
   - subjects: Parte de la base de conocimiento con la información de las asignaturas.



- src/
   - inference_engine.py: Implementación del modo CoT 
   - rag.py: Implementación del módulo de RAG
   - utils.py: Utilidades para procesar la base de conocimiento.



- main.py: Punto de entrada principal del proyecto.

- requirements.txt: Lista de dependencias necesarias.

- pyproject.toml: Archivo de configuración del proyecto.

- uv.lock: Archivo de bloqueo para la gestión de dependencias.

## 🛠️ Instalación y Configuración

Asegúrate de tener instalado lo siguiente en tu sistema:
- Python 3.8 o superior
- Las dependencias del proyecto listadas en `requirements.txt`
    ```bash
    pip install -r requirements.txt
Las dependencias incluyen:

- `click`: Para la interfaz de línea de comandos.
- `ollama`: Cliente para interactuar con modelos de Ollama. Este proyecto utiliza el modelo `llama3.2:1b` de Ollama. Asegúrate de que el modelo esté instalado en tu entorno antes de continuar.
- `uv`: Para ejecutar scripts desde un entorno virtual.

### Cómo ejecutar el programa

1. Abre una terminal o consola de comandos.
2. Navega a la carpeta donde se encuentra el archivo `main.py` usando el comando `cd`.
     ```bash
     cd /ruta/a/tu/proyecto
     ```
3. Ejecuta el programa con el siguiente comando:  
   ```bash
   uv run python main.py knowledge_base

4. Opciones Adicionales:

El asistente acepta las siguientes opciones:

- `--model`: Especifica el modelo de lenguaje a utilizar (por defecto: llama3.2:1b).
- `--mode`: Define el modo de operación. Los valores posibles son:
   - rag: Recupera contexto relevante antes de generar una respuesta.
   - cot: Simula razonamiento paso a paso antes de responder.
- `--verbose`: Muestra detalles adicionales del proceso de ejecución.

Ejemplo:
```bash
uv run python main.py knowledge_base --mode=cot --verbose
```

## 🧠 Modos de Operación

### RAG (Retrieve and Generate)
En este modo, el asistente busca fragmentos relevantes de la base de conocimiento y los utiliza para responder la consulta del usuario.

### Chain of Thought (CoT)
En este modo, el asistente simula un proceso de razonamiento antes de responder. Genera pasos intermedios para analizar la consulta y organizar su respuesta de manera estructurada.

## 📚 Base de Conocimiento
Los archivos de la carpeta `knowledge_base` contienen información estructurada sobre profesores, estudiantes y asignaturas. Durante la ejecución, esta información es procesada para extraer palabras clave y contextos relevantes.

## 🧪 Ejemplos de Consultas
Al ejecutar el asistente, puedes realizar preguntas como:
- Which courses does Juan Perez take?
- Tell me about Modern Physics.
- Who teaches Data Structures and Algorithms?

## 👥 Integrantes

- Mario López Díaz
- Ignacio Gutiérrez Sánchez