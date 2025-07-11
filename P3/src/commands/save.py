import click


@click.command()
@click.argument("filename")
def save(filename, kb_manager):
    """Guarda la base de conocimiento en un archivo."""
    try:
        # Validar el nombre del archivo
        if not filename.strip():
            click.echo("Error: El nombre del archivo no puede estar vacío.")
            return

        kb = kb_manager.get_kb()
        if not kb.data:
            click.echo("Advertencia: La base de conocimiento está vacía. No se guardará nada.")
            return

        try:
            # Intentar guardar los datos en el archivo
            with open(filename, "w") as file:
                equivalents = kb.get_equivalents()

                file.write('# Base de conocimiento guardada \n')
                # Guardar los datos de kb.data
                for subject, predicates in kb.data.items():
                    for predicate, objects in predicates.items():
                        for obj in objects:
                            file.write(f'{subject} {predicate} "{obj}" .\n')

                file.write('# Propiedades de equivalencia\n')
                # Guardar los equivalentes en el formato deseado
                for equivalent_set in equivalents:
                    for i in range(len(equivalent_set) - 1):
                        subject = list(equivalent_set)[i]
                        object_ = list(equivalent_set)[i + 1]
                        file.write(f'{subject} wdt:P1628 {object_} .\n')

            click.echo(f"Base de conocimiento guardada en {filename}.")
        except IOError as e:
            click.echo(f"Error: No se pudo escribir en el archivo '{filename}'. Detalle: {e}")
        except Exception as e:
            click.echo(f"Error inesperado al guardar la base de conocimiento. Detalle: {e}")

        # Actualizar el gestor de la base de conocimiento
        kb_manager.set_kb(kb)
    except AttributeError as e:
        click.echo(f"Error: Problema al acceder a la base de conocimiento. Detalle: {e}")
    except Exception as e:
        click.echo(f"Error inesperado durante la operación de guardado. Detalle: {e}")
