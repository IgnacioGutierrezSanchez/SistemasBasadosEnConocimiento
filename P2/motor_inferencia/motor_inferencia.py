from functools import reduce  # Para aplicar lógicas difusas como suma/producto

class MotorInferencia:
    def __init__(self, archivo_bc, config):
        self.reglas = []
        self.hechos = {}
        self.config = config
        self.cargar_base_conocimiento(archivo_bc)

    def cargar_base_conocimiento(self, archivo_bc):
        """Cargar la base de conocimiento desde un archivo."""
        with open(archivo_bc, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue

                if ":-" in linea:  # Es una regla
                    cons, antecedentes = linea.split(":-")
                    cons = cons.strip()
                    if '[' in antecedentes:  # Con grado de verdad
                        antecedentes, grado_verdad = antecedentes.split('[')
                        antecedentes = antecedentes.strip().split(',')
                        grado_verdad = float(grado_verdad.strip(']'))
                    else:
                        antecedentes = antecedentes.strip().split(',')
                        grado_verdad = 1.0  # Valor por defecto

                    antecedentes = [a.strip() for a in antecedentes]
                    self.reglas.append((cons, antecedentes, grado_verdad))

                else:  # Es un hecho
                    if '[' in linea:
                        hecho, grado_verdad = linea.split('[')
                        hecho = hecho.strip()
                        grado_verdad = float(grado_verdad.strip(']'))
                    else:
                        hecho = linea.strip()
                        grado_verdad = 1.0  # Valor por defecto

                    self.hechos[hecho] = grado_verdad

    def print_base_conocimiento(self):
        """Imprimir la base de conocimiento actual."""
        print("Reglas:")
        for cons, antecedentes, grado_verdad in self.reglas:
            antecedentes_str = ", ".join(antecedentes)
            print(f"{cons} :- {antecedentes_str} [{grado_verdad}]")

        print("\nHechos:")
        for hecho, grado_verdad in self.hechos.items():
            print(f"{hecho} [{grado_verdad}]")

    def add_hecho(self, hecho, grado_verdad):
        """Agregar un nuevo hecho a la base de conocimiento."""
        self.hechos[hecho] = grado_verdad
        print(f"Hecho '{hecho}' agregado con grado de verdad {grado_verdad}.")

    def aplicar_logica_difusa(self, grados):
        """Aplicar la lógica difusa configurada (min/max o suma/producto)."""
        logica = self.config['logica_difusa']
        if logica == 'min_max':
            return min(grados)  # Min/Max
        elif logica == 'suma':
            return sum(grados) / len(grados)  # Promedio (suma)
        elif logica == 'producto':
            return reduce(lambda x, y: x * y, grados)  # Producto
        else:
            raise ValueError("Lógica difusa no reconocida.")

    def backward_chain(self, consulta, reglas_aplicadas=None):
        """Implementar el razonamiento hacia atrás."""
        if consulta in self.hechos:
            return self.hechos[consulta], reglas_aplicadas

        if reglas_aplicadas is None:
            reglas_aplicadas = []

        for cons, antecedentes, grado_verdad in self.reglas:
            if cons == consulta:
                grados = []
                for antecedente in antecedentes:
                    grado_antecedente, reglas_antecedente = self.backward_chain(antecedente, reglas_aplicadas)
                    if grado_antecedente is None:
                        break
                    grados.append(grado_antecedente)

                if len(grados) == len(antecedentes):
                    grado_combinado = self.aplicar_logica_difusa(grados)
                    resultado = min(grado_verdad, grado_combinado)
                    self.hechos[consulta] = resultado
                    reglas_aplicadas.append(f"{cons} :- {', '.join(antecedentes)} [{grado_verdad}]")
                    return resultado, reglas_aplicadas

        return None, reglas_aplicadas