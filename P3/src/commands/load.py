import click
from ..core.rdf_parser import parse_rdf_file

@click.command()
@click.argument("filenames")
def load(filenames, kb_manager):
    """Carga uno o varios archivos RDF en la base de conocimiento."""
    try:
        kb = kb_manager.get_kb()
        filenames = filenames.split()

        if not filenames:
            click.echo("Error: No se especificaron archivos RDF para cargar.")
            return

        for filename in filenames:
            try:
                # Intentar parsear y cargar el archivo RDF
                triples = parse_rdf_file(filename, kb)
                kb.load_triples(triples)
            except FileNotFoundError:
                click.echo(f"Error: El archivo '{filename}' no se encontró.")
            except ValueError as ve:
                click.echo(f"Error: Problema al parsear el archivo '{filename}'. Detalle: {ve}")
            except Exception as e:
                click.echo(f"Error inesperado al cargar el archivo '{filename}'. Detalle: {e}")

        kb_manager.set_kb(kb)

    except AttributeError as e:
        click.echo(f"Error: Problema al acceder a la base de conocimiento. Detalle: {e}")
    except Exception as e:
        click.echo(f"Error inesperado durante la carga de archivos RDF. Detalle: {e}")
