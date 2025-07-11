import click

@click.command()
def help(text, kb_manager):
    """Muestra los comandos disponibles."""
    print(
        "Comandos disponibles:\n"
        "  load <archivo1> <archivo2> ...       - Carga uno o varios archivos RDF\n"
        "  query/select <consulta SPARQL>       - Realiza una consulta SPARQL\n"
        "  add <sujeto> <predicado> <objeto>    - Agrega una nueva tripleta\n"
        "  save <archivo>                       - Guarda la base de conocimiento en un archivo\n"
        "  draw                                 - Dibuja el grafo de la última consulta\n"
        "  exit                                 - Salir del modo interactivo\n"
        "  help                                 - Muestra este mensaje\n\n"
        "Comandos implementados para la gestion de errores al cargar la base de datos:\n"
        "  show                                 - Muestra la/s base/s de conocimiento cargadas y su numero de lineas.\n"
        "                                         Ademas se diferencian las propiedades de equivalencia guardadas\n"
        "  contar <archivo1>                    - Muestra las lineas de la base de conocimiento seleccionada"

    )
