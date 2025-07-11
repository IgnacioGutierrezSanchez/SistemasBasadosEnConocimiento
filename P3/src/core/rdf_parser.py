import re

def parse_rdf_file(filename, kb):
    triples = []
    subject = None

    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                    line = line.strip()
                    if line.startswith("#") or not line:
                        continue  # Ignorar comentarios y líneas vacías

                    if "wdt:P1628" in line:  # Procesar equivalencia
                        subject, obj = process_equivalence(line, kb)
                        if subject and obj:
                            kb.add_equivalent_property(subject, obj)

                    elif re.match(r"^q9:", line):  # Procesar tripletas con sujeto q9:
                        subject, new_triples = process_triples(line)
                        triples.extend(new_triples)

                    elif subject:  # Continuación de tripletas del sujeto anterior
                        new_triples = process_property_line(line, subject)
                        triples.extend(new_triples)
                except Exception as e:
                    print(f"Error procesando la línea '{line}': {e}")
    except FileNotFoundError:
        print(f"El archivo '{filename}' no se encuentra.")
    except Exception as e:
        print(f"Error al leer el archivo '{filename}': {e}")

    print("Carga de archivos completada.")
    return triples

def process_equivalence(line, kb):
    """Procesa líneas que contienen 'wdt:P1628' y genera equivalencia."""
    try:
        parts = []
        refactor_parts(line, parts)
        subject = parts[0].split()[0]
        obj = parts[0].split()[2]
        return subject, obj
    except IndexError as e:
        print(f"Error procesando equivalencia en la línea '{line}': {e}")
        return None, None
    except Exception as e:
        print(f"Error inesperado en process_equivalence para la línea '{line}': {e}")
        return None, None

def process_triples(line):
    """Procesa líneas con sujetos q9: y extrae las tripletas."""
    try:
        parts = []
        refactor_parts(line, parts)
        subject = parts[0].split()[0]  # Obtener sujeto
        triples = []

        for part in parts:
            if part:
                match = re.match(r"(\S+)\s+(\S+)\s+(.+)", part)
                if match:
                    _, predicate, obj = match.groups()
                    obj = obj.strip('"')  # Eliminar comillas
                    triples.append((subject, predicate, obj))

        return subject, triples
    except Exception as e:
        print(f"Error procesando triples en la línea '{line}': {e}")
        return None, []

def process_property_line(line, subject):
    """Procesa líneas de propiedades relacionadas con un sujeto."""
    try:
        match = re.match(r"(\S+)\s+(.+)", line)
        triples = []

        if match:
            predicate, obj = match.groups()
            obj = obj.strip('"')  # Eliminar comillas
            triples.append((subject, predicate, obj))

        return triples
    except Exception as e:
        print(f"Error procesando propiedades en la línea '{line}': {e}")
        return []

def refactor_parts(line, parts):
    """Refactoriza una línea añadiendo partes en caso de terminación con punto."""
    try:
        if line.endswith("."):
            parts.append(line[:-1])  # Elimina el punto final
            parts.append("")  # Parte vacía
        else:
            parts.append(line)  # Agrega la línea sin cambios

        parts[0] = parts[0][:-1]  # Elimina el punto al final de la primera parte
    except Exception as e:
        print(f"Error refactorizando partes de la línea '{line}': {e}")
