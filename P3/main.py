import click
from src.commands.cli import interactive

if __name__ == "__main__":
    # Mostrar un mensaje inicial y ejecutar el modo interactivo
    click.echo("Entrando en modo interactivo. Escribe 'help' para ver los comandos disponibles.")
    interactive()
