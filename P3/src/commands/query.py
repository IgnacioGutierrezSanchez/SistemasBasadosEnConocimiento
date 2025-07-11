import click

@click.command()
@click.argument("query_text")
def query(query_text, kb_manager):
    """Realiza una consulta SPARQL en la base de conocimiento."""
    try:
        engine = kb_manager.get_engine()

        if not query_text.strip():
            click.echo("Error: La consulta SPARQL no puede estar vacía.")
            return

        try:
            # Intentar ejecutar la consulta
            engine.execute_query(query_text)
            click.echo("Consulta ejecutada con éxito.")
        except SyntaxError as se:
            click.echo(f"Error de sintaxis en la consulta SPARQL. Detalle: {se}")
        except ValueError as ve:
            click.echo(f"Error: La consulta SPARQL no es válida. Detalle: {ve}")
        except Exception as e:
            click.echo(f"Error inesperado durante la ejecución de la consulta. Detalle: {e}")

        kb_manager.set_engine(engine)

    except AttributeError as e:
        click.echo(f"Error: Problema al acceder al motor de consultas. Detalle: {e}")
    except Exception as e:
        click.echo(f"Error inesperado al procesar la consulta SPARQL. Detalle: {e}")
