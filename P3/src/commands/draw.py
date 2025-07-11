import click

@click.command()
def draw(texto, kb_manager):
    """Genera un grafo a partir de la última consulta SPARQL realizada."""
    try:
        engine = kb_manager.get_engine()

        # Verificar si hay resultados recientes para graficar
        if not engine.last_query_results:
            click.echo("Error: No se ha ejecutado ninguna consulta SPARQL reciente. No hay datos para graficar.")
            return

        # Intentar generar el grafo
        engine.draw()

    except AttributeError as e:
        click.echo(f"Error: Problema al acceder al motor de consultas o a los resultados. Detalle: {e}")
    except Exception as e:
        click.echo(f"Error inesperado al intentar generar el grafo. Detalle: {e}")
