import click

@click.command()
@click.argument("text")
def add(text, kb_manager):
    """Agrega una nueva tripleta a la base de conocimiento."""
    kb = kb_manager.get_kb()

    try:
        # Comprobar si el texto contiene exactamente tres elementos
        aux = text.split()
        if len(aux) != 3:
            raise ValueError(
                "La entrada debe contener exactamente tres elementos: sujeto, predicado y objeto."
            )

        # Asignar elementos de la tripleta
        subject, predicate, object = aux

        # Verificar que los elementos no estén vacíos
        if not all([subject.strip(), predicate.strip(), object.strip()]):
            raise ValueError(
                "Ningún elemento de la tripleta puede estar vacío. Asegúrate de incluir valores válidos."
            )

        # Intentar agregar la tripleta a la base de conocimiento
        kb.add_triple(subject, predicate, object)
        kb_manager.set_kb(kb)

        print(f"Tripleta agregada: {subject} {predicate} {object}.")

    except ValueError as ve:
        print(f"Error: {ve}")

    except Exception as e:
        print(f"Error inesperado al agregar la tripleta: {e}")
