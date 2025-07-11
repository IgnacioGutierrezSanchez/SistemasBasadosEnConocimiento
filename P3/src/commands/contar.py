import click

@click.command()
@click.argument("filename")
def contar(filename, kb_manager):
    """Cuenta las líneas de un archivo, excluyendo las que comienzan con #"""
    lineas_sin_comentarios = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if not line.startswith("#") and line.strip():  # Ignorar líneas que comienzan con # y vacias
                    lineas_sin_comentarios += 1

        print(f"El archivo '{filename}' tiene {lineas_sin_comentarios} líneas sin comentarios.")

    except FileNotFoundError:
        print(f"El archivo '{filename}' no se encuentra.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")