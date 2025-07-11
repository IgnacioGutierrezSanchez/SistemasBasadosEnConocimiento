import click
import pathlib
from motor_inferencia.motor_inferencia import MotorInferencia
from motor_inferencia.utils import add, pregunta

try:
    import tomllib  # Disponible desde Python 3.11
except ImportError:
    import toml as tomllib  # Fallback a toml para versiones anteriores


def cargar_configuracion(config_path):
    """Cargar configuración desde un archivo .toml o usar valores por defecto."""
    configuracion_default = {
        'logica_difusa': 'min_max',
        'rangos_respuesta': {
            'mucho': 0.75,
            'algo': 0.5,
            'poco': 0.25,
        }
    }
    if config_path and config_path.exists():
        try:
            configuracion = tomllib.loads(config_path.read_text())
            print(f"Cargando configuración desde {config_path}")
        except Exception as e:
            print(f"Error al cargar el archivo de configuración: {e}")
            configuracion = configuracion_default
    else:
        configuracion = configuracion_default
        print("Usando configuración por defecto.")
    return configuracion


@click.command()
@click.argument('base_name')  # Nombre de la base de conocimiento sin la ruta
@click.option('--config', type=pathlib.Path, default=pathlib.Path('config.toml'), help='Fichero de configuración .toml')
def main(base_name, config):
    """Inicializar el motor de inferencia y procesar comandos interactivos."""
    # Ruta base de las bases de conocimiento
    base_dir = pathlib.Path('basesConocimiento')
    archivo_bc = base_dir / base_name

    if not archivo_bc.exists():
        print(f"Error: La base de conocimiento '{archivo_bc}' no existe.")
        return

    # Cargar configuración
    configuracion = cargar_configuracion(config)

    # Inicializar motor de inferencia
    motor = MotorInferencia(archivo_bc, configuracion)

    # Loop de comandos interactivos
    while True:
        entrada = input("> ").strip()

        if entrada == "quit":
            print("Saliendo del programa.")
            break
        elif entrada == "print":
            motor.print_base_conocimiento()
        elif entrada.startswith("add "):
            add(entrada, motor)
        elif entrada.endswith("?"):
            consulta = entrada.strip("?")
            grado_verdad, reglas_aplicadas = motor.backward_chain(consulta)
            pregunta(entrada, consulta, grado_verdad, reglas_aplicadas, configuracion)
        else:
            print("Comando no reconocido.")


if __name__ == "__main__":
    main()
