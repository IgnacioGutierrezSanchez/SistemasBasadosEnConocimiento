import click

@click.command()
def show(texto, kb_manager):
    kb = kb_manager.get_kb()
    kb.show()