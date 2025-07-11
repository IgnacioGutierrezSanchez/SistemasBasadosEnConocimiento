import click
from .load import load
from .query import query
from .save import save
from .add import add
from .draw import draw
from .help import help
from .show import show
from .contar import contar
from ..core.sparql_engine import QueryEngine
from ..core.data_store import KnowledgeBase

# Instanciar KnowledgeBase y QueryEngine
kb = KnowledgeBase()
engine = QueryEngine(kb)

# Crear una instancia global de KnowledgeBaseManager
class KnowledgeBaseManager:
    def __init__(self, kb: KnowledgeBase, engine: QueryEngine):
        self._kb = kb
        self._engine = engine

    def get_kb(self):
        return self._kb

    def set_kb(self, kb: KnowledgeBase):
        self._kb = kb

    def get_engine(self):
        return self._engine

    def set_engine(self, engine: QueryEngine):
        self._engine = engine

# Crear una instancia de KnowledgeBaseManager
kb_manager = KnowledgeBaseManager(kb, engine)

@click.group()
def cli():
    """CLI para gestionar redes semánticas."""
    pass

# Registrar los comandos
cli.add_command(load)
cli.add_command(query)
cli.add_command(save)
cli.add_command(add)
cli.add_command(draw)
cli.add_command(help)
cli.add_command(show)
cli.add_command(contar)

def interactive():
    """Modo interactivo para cargar archivos y hacer consultas."""
    while True:
        command = input(">> ").strip()
        if not command:
            continue

        if ' ' in command:  # Si el comando contiene al menos un espacio
            if "select" in command and not command.startswith("query"):
                command_name = "query"
                args = [command]
            else:
                command_name, args = command.split(' ', 1)  # Divide solo por el primer espacio
                args = [args]
        else:
            command_name = command  # Si no hay espacio, el comando es todo
            args = ['']  # No hay argumentos

        if command_name.lower() in ["exit", "quit"]:
            click.echo("Saliendo del modo interactivo.")
            break
        else:
            # Intentar invocar el comando correspondiente
            command_cli = cli.get_command(None, command_name)
            if command_cli:
                try:
                    # Ejecutar el comando con los argumentos
                    command_cli.callback(*args, kb_manager=kb_manager)
                except Exception as e:
                    click.echo(f"Error ejecutando el comando '{command_name}': {e}")
            else:
                click.echo(
                    f"Comando no reconocido: {command_name}. Escribe 'help' para ver los comandos disponibles."
                )
