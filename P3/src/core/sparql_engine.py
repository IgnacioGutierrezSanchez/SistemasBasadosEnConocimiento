import re
import networkx as nx
from .graphs import crear_grafo


class QueryEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.last_query_results = (
            []
        )  # Para almacenar los resultados de la última consulta

    def execute_query(self, query):
        # Parsear consulta para obtener variables y patrones
        select_match = re.search(
            r"select\s+(.+?)\s+where\s*\{(.+?)\}", query, re.DOTALL
        )
        if not select_match:
            raise ValueError("Consulta SPARQL no válida.")

        # Extraer variables y patrones de la consulta
        variables = [var.strip(",") for var in select_match.group(1).split()]
        patterns_text = select_match.group(2).strip()
        patterns = [
            pattern.strip()
            for pattern in re.split(r"\.\s*", patterns_text)
            if pattern.strip()
        ]

        # Procesar cada patrón en la consulta
        intermediate_results = []  # Resultados intermedios por patrón

        for pattern in patterns:
            parts = pattern.split()
            if len(parts) != 3:
                continue  # Saltar patrones mal formados

            subj, pred, obj = parts
            # Obtener las propiedades equivalentes para el predicado
            predicates_to_check = (
                self.kb.get_equivalent_properties(pred)
                if not pred.startswith("?")
                else [pred]
            )
            matches = []

            for check_pred in predicates_to_check:
                matches += self.kb.find(
                    subject=None if subj.startswith("?") else subj,
                    predicate=None if check_pred.startswith("?") else check_pred,
                    obj=None if obj.startswith("?") else obj,
                )

            # Almacenar coincidencias parciales
            filtered_results = []
            for match in matches:
                result = {}
                if subj.startswith("?"):
                    result[subj] = match[0]
                if pred.startswith("?"):
                    result[pred] = match[1]
                if obj.startswith("?"):
                    result[obj] = match[2]
                if result:
                    filtered_results.append(result)

            intermediate_results.append(filtered_results)

        # Combinar resultados de cada patrón
        final_results = self._merge_results(intermediate_results, variables)
        # Almacenar los resultados finales
        self.last_query_results = final_results
        # Imprimir resultados
        self._print_results(variables, final_results)

    def _merge_results(self, intermediate_results, variables):
        """Combina los resultados intermedios para generar resultados finales."""
        try:
            merged_results = []

            if intermediate_results:
                # Empezar con el primer conjunto de resultados y combinar progresivamente
                merged_results = intermediate_results[0]

                for result_set in intermediate_results[1:]:
                    temp_results = []
                    for res1 in merged_results:
                        for res2 in result_set:
                            # Revisar si las variables comunes coinciden
                            if all(
                                    res1.get(key) == res2.get(key, res1.get(key))
                                    for key in res1.keys()
                            ):
                                combined = {**res1, **res2}
                                temp_results.append(combined)
                    merged_results = temp_results

            # Filtrar para las variables seleccionadas y limpiar valores
            final_results = []
            for result in merged_results:
                final_results.append(
                    [self._clean_value(result.get(var, "")) for var in variables]
                )

            return final_results

        except Exception as e:
            print(f"Error al combinar los resultados: {str(e)}")
            return []

    def _print_results(self, variables, results):
        # Calcular el ancho máximo de cada columna
        column_widths = [
            max(len(str(value)) for value in col)
            for col in zip(*([variables] + results))
        ]

        # Crear una fila formateada para el encabezado
        header = " | ".join(
            f"{var:<{column_widths[i]}}" for i, var in enumerate(variables)
        )
        separator = "|".join("-" * (width + 2) for width in column_widths)

        # Imprimir el encabezado y el separador
        print(f"| {header} |")
        print(f"|{separator}|")

        # Imprimir cada fila con el ancho adecuado
        for result in results:
            # Limpiar los valores antes de imprimir
            row = " | ".join(
                f"{self._clean_value(value):<{column_widths[i]}}"
                for i, value in enumerate(result)
            )
            print(f"| {row} |")

    def _clean_value(self, value):
        """Elimina las comillas, el punto final y el punto y coma de los valores."""
        try:
            if not isinstance(value, str):
                raise TypeError(f"Valor no es una cadena de texto: {value}")

            value = value.strip()  # Elimina los espacios al principio y al final
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]  # Elimina las comillas
            if value.endswith("."):
                value = value[:-1]  # Elimina el punto final
            if value.endswith(";"):
                value = value[:-1]  # Elimina el punto y coma
            return value
        except Exception as e:
            print(f"Error al limpiar el valor: {str(e)}")
            return value

    def draw(self):
        """Dibuja el grafo de la última consulta ejecutada y lo guarda como imagen PNG."""
        try:
            if not self.last_query_results:
                print("No hay resultados de consulta para dibujar.")
                return

            # Crear un grafo dirigido
            G = nx.DiGraph()

            # Detectar el número de columnas en los resultados
            num_columns = (
                len(self.last_query_results[0])
                if isinstance(self.last_query_results[0], list)
                else len(self.last_query_results[0].keys())
            )
            column_names = [f"?var{i}" for i in range(num_columns)]

            # Iterar sobre los resultados de la última consulta
            for result in self.last_query_results:
                if isinstance(result, dict):
                    # Si el resultado es un diccionario, obtenemos las variables directamente
                    values = [result.get(key) for key in result]
                else:
                    # Si el resultado es una lista, usamos la lista directamente
                    values = result

                # Añadir nodos y aristas en función del número de columnas en el resultado
                if num_columns == 2:
                    # Si hay dos columnas, se crea una arista punteada entre el primer nodo y el segundo
                    G.add_edge(values[0], values[1], style="dotted", color="blue")
                elif num_columns == 3:
                    # Si hay tres columnas, se añade una arista sólida con el nombre del predicado como etiqueta
                    G.add_edge(
                        values[0], values[2], label=values[1], style="solid", color="green"
                    )
                else:
                    print("Formato de resultado no compatible para el dibujo.")
                    return

            # Crear el grafo
            crear_grafo(G)

        except Exception as e:
            print(f"Error al dibujar el grafo: {str(e)}")
