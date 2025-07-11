# Sistemas Basados en Conocimiento - Prácticas

Este repositorio contiene las prácticas realizadas en la asignatura **Sistemas Basados en Conocimiento**, del Grado en Ingeniería de Datos e Inteligencia Artificial. A lo largo del curso, desarrollamos diferentes aplicaciones relacionadas con la representación del conocimiento, el razonamiento automático y los sistemas inteligentes aplicados a dominios como lógica difusa, redes semánticas y modelos de lenguaje.

## Contenido del repositorio

### Práctica 2: Sistema Basado en Conocimiento con Lógica Difusa

Esta práctica consiste en la implementación de un motor de inferencia que utiliza lógica difusa para razonar sobre hechos y reglas. El sistema permite:

- Agregar hechos con distintos grados de verdad.
- Consultar hechos mediante razonamiento hacia atrás.
- Cargar distintas bases de conocimiento desde archivos.
- Configurar el comportamiento de la lógica difusa mediante archivos TOML.

**Estructura principal:**
- `motor_inferencia/`: Código fuente del motor de inferencia.
- `basesConocimiento/`: Bases de conocimiento para distintos dominios (laboral, enfermedades).
- `main.py`: Archivo principal del sistema.
- `config.toml`: Parámetros de la lógica difusa.

**Ejemplo de uso:**
```bash uv run python main.py base_laboral.txt```

Práctica 3: Gestión de Redes Semánticas con RDF y SPARQL
En esta práctica se construyó una herramienta modular en terminal para gestionar redes semánticas. Se trabajó con archivos RDF y se implementó un motor SPARQL básico que permite:

- Cargar uno o varios archivos RDF.
- Realizar consultas SPARQL.
- Agregar nuevas tripletas.
- Visualizar resultados como grafos.
- Guardar y mostrar bases de conocimiento.

Estructura principal:
`src/`: Contiene todos los comandos y lógica del sistema.
`data/`: Bases de conocimiento RDF (académica y laboral).
`ejemplosEjecucion/`: Archivos de ejemplo.
`main.py`: Punto de entrada del sistema.

**Ejemplo de uso:**
```bash uv run main.py interactive```

Práctica 4: Asistente Académico basado en Modelos de Lenguaje
Se desarrolló un asistente virtual que responde a preguntas sobre un dominio académico utilizando un modelo de lenguaje (LLaMA3 1b) a través de Ollama. El sistema tiene dos modos:

- RAG (Retrieve and Generate): Recupera información relevante de la base antes de generar la respuesta.
- CoT (Chain of Thought): Simula un razonamiento paso a paso antes de responder.

Estructura principal:
`src/`: Implementación de RAG, CoT e inferencia.
`knowledge_base/`: Archivos de conocimiento con información sobre profesores, estudiantes y asignaturas.
`main.py`: Punto de entrada del sistema.

**Ejemplo de uso:**
```bash uv run python main.py knowledge_base --mode=cot --verbose```

Estudiantes:
- Ignacio Gutiérrez Sánchez
- Mario López Díaz
