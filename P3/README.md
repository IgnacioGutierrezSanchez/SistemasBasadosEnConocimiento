# PRÁCTICA 3: Gestión de Redes Semánticas

Este proyecto es una herramienta de terminal que permite gestionar y consultar redes semánticas utilizando RDF y SPARQL. Incluye funcionalidades para cargar bases de conocimiento, realizar consultas, visualizar resultados como grafos y guardar datos procesados. El proyecto está diseñado para ser modular y extensible, con soporte para equivalencias de propiedades y procesamiento de múltiples formatos RDF.

## Estructura del repositorio
La estructura del proyecto es la siguiente:

- data/
   - RedAcademica.txt: Base de conocimiento de la red académica.
   - RedLaboral.txt: Base de conocimiento de la red laboral.


- ejemplosEjecucion/
   - EjemploRedAcademica.txt: Ejemplo de ejecución para la red académica. 
   - EjemploRedLaboral.txt: Ejemplo de ejecución para la red laboral.

- src/
  - commands/
    - cli.py: Gestiona la interfaz de línea de comandos interactiva y modular
    - load.py: Carga uno o varios archivos RDF.
    - query.py: Realiza una consulta SPARQL.
    - add.py: Agrega una nueva tripleta.
    - save.py: Guarda la base de conocimiento en un archivo.
    - draw.py: Dibuja el grafo de la última consulta.
    - help.py: Muestra el mensaje de ayuda.
    - show.py: Muestra las bases de conocimiento cargadas y sus líneas, diferenciando propiedades de equivalencia.
    - contar.py: Muestra las líneas de una base de conocimiento seleccionada.
  - core/
    - data_store.py: Implementación de la clase KnowledgeBase. 
    - graphs.py: Funciones para visualizar los grafos.
    - rdf_parser.py: Parser de archivos RDF.
    - sparql_engine.py: Motor de consultas SPARQL.

- main.py: Punto de entrada principal del proyecto.

- requirements.txt: Lista de dependencias necesarias.

- pyproject.toml: Archivo de configuración del proyecto.

## Requisitos

Asegúrate de tener instalado lo siguiente en tu sistema:
- Python 3.8 o superior
- Las dependencias del proyecto listadas en `requirements.txt`
    ```bash
    pip install -r requirements.txt

### Cómo ejecutar el programa

1. Abre una terminal o consola de comandos.
2. Navega a la carpeta donde se encuentra el archivo `main.py` usando el comando `cd`.
     ```bash
     cd /ruta/a/tu/proyecto
     ```
3. Crea un entorno virtual y actívalo:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

4. Ejecuta el programa con el siguiente comando:  
   ```bash
   uv run main.py interactive

### Interacción en la consola

Después de ejecutar el programa en **modo interactivo**, puedes utilizar los siguientes comandos para cargar datos, realizar consultas y gestionar la base de conocimiento:

### Comandos disponibles

#### Cargar archivos RDF
Permite cargar uno o más archivos RDF en la base de conocimiento.

- **Formato**: `load <archivo1> <archivo2> ...`
- **Ejemplo**: 
  ```sparql
  load data/ejemplo.rdf

---

#### Realizar una consulta SPARQL
Ejecuta consultas SPARQL sobre la base de conocimiento.

- **Formato**: `query <consulta SPARQL>`
- **Ejemplo**:
  ```sparql
  query SELECT ?s WHERE { ?s ?p ?o . }

---

#### Agregar una nueva tripleta
Agrega manualmente una tripleta a la base de conocimiento.

- **Formato**: `add <sujeto> <predicado> <objeto>`
- **Ejemplo**:
  ```sparql
  add q9:estudiante1 t9:nombre "Juan Lopez"

---

#### Guardar la base de conocimiento
Guarda el contenido actual de la base de conocimiento en un archivo.

- **Formato**: `save <archivo>`
- **Ejemplo**:
  ```sparql
  save nueva_base.txt

---

#### Dibujar el grafo
Genera una representación gráfica del resultado de la última consulta SPARQL ejecutada.

- **Formato**: `draw`
- **Nota**: Este comando solo funciona si hay resultados de una consulta SPARQL previa.

---

#### Mostrar ayuda
Muestra la lista de comando disponible.

- **Formato**: `help`

---

#### Salir del modo interactivo
Finaliza la ejecución del modo interactivo.

- **Formato**: `exit` o `quit`



### Integrantes

- Mario López Díaz
- Ignacio Gutiérrez Sánchez
