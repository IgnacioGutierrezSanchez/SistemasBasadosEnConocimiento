# PRÁCTICA 2: Sistema Basado en Conocimiento con Lógica Difusa

Este proyecto implementa un Sistema Basado en Conocimiento (SBC) con un motor de inferencia que utiliza lógica difusa para deducir hechos a partir de una base de reglas. El sistema permite agregar hechos, imprimir la base de conocimiento y realizar consultas mediante razonamiento hacia atrás.

## Estructura del repositorio

El repositorio está compuesto por los siguientes archivos:

- **basesConocimiento/**: Carpeta que contiene las bases de conocimiento utilizadas por el sistema:
  - `base_laboral`: Contiene una base de conocimiento enfocada en la adquisición de talento, con reglas sobre trabajos y habilidades.
  - `base_enfermedades`: Contiene una base de conocimiento sobre enfermedades y sus respectivos síntomas.
  
- **motor_inferencia/**: Carpeta que contiene el código fuente del motor de inferencia:
  - `motor_inferencia.py`: Implementación principal del motor de inferencia basado en lógica difusa.
  - `utils.py`: Funciones auxiliares para manipular hechos y consultas.

- **main.py**: Archivo principal para la ejecución del sistema. Permite cargar bases de conocimiento desde la carpeta `basesConocimiento` y procesar comandos interactivos.

- **config.toml**: Archivo de configuración para definir el tipo de lógica difusa y los rangos de respuesta.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.7 o superior** (Python 3.11 recomendado para compatibilidad con `tomllib`)
- Las siguientes bibliotecas de Python:
  - `click`
  - `uv`
  - `tomllib` (para Python 3.11+) o `tomli` (para versiones anteriores a Python 3.11)

### Instalación de dependencias

Puedes instalar las dependencias necesarias ejecutando:

pip install click tomli    # Para Python 3.10 o versiones anteriores

## Ejecución del código

El programa se ejecuta utilizando el archivo `main.py`, especificando el nombre de una base de conocimiento dentro de la carpeta `basesConocimiento`.

### Ejemplo de ejecución básica

```bash
uv run python main.py base_laboral.txt
```

### Ejecución con archivo de configuración

Puedes proporcionar un archivo TOML de configuración utilizando la opción `--config`.

Esto es útil si deseas personalizar los parámetros de la lógica difusa y los rangos de respuesta:

```bash
uv run python main.py <archivo_bc> --config <archivo_config.toml>
```
  - `<archivo_bc>`: Nombre del archivo que contiene la base de conocimiento.
  - `<archivo_config.toml>`: Archivo de configuración en formato TOML.

### Interacción en la consola

Después de ejecutar el programa, puedes interactuar con él utilizando los siguientes comandos en la consola:

  - Agregar un hecho: Para agregar un nuevo hecho a la base de conocimiento. 
    - Formato: add `<hecho>` [grado_de_verdad]
    - Ejemplo: add profesor [0.8]

  - Realizar una consulta: Para preguntar si un hecho es cierto.
    - Formato: `<hecho>`?
    - Ejemplo: lluvia?

  - Imprimir la base de conocimiento: Para mostrar todas las reglas y hechos cargados en la base de conocimiento.
    - Comando: print
      
  - Salir del programa: Para finalizar la ejecución.
    - Comando: quit.

### Estudiantes

- Mario López Díaz
- Ignacio Gutiérrez Sánchez
