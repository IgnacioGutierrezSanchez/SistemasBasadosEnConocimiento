class KnowledgeBase:
    def __init__(self):
        try:
            self.data = {}
            self.equivalents = []  # Lista de conjuntos para relaciones de equivalencias
        except Exception as e:
            print(f"Error al inicializar KnowledgeBase: {e}")

    def get_equivalents(self):
        return self.equivalents

    def add_triple(self, subject, predicate, obj):
        """Agrega una tripleta a la estructura de datos en memoria."""
        try:
            if predicate == "wdt:P1628":
                self.add_equivalent_property(subject, obj)
            else:
                if subject not in self.data:
                    self.data[subject] = {}
                if predicate not in self.data[subject]:
                    self.data[subject][predicate] = []
                self.data[subject][predicate].append(obj)
        except Exception as e:
            print(f"Error al agregar tripleta ({subject}, {predicate}, {obj}): {e}")

    def load_triples(self, triples):
        """Carga una lista de tripletas a la base de conocimiento y agrega equivalencias si el predicado es P1628."""
        try:
            for subject, predicate, obj in triples:
                self.add_triple(subject, predicate, obj)
        except Exception as e:
            print(f"Error al cargar tripletas: {e}")

    def add_equivalent_property(self, prop1, prop2):
        """Registra dos propiedades como equivalentes solo si están relacionadas por P1628."""
        try:
            for equivalent_set in self.equivalents:
                # Si prop1 o prop2 ya está en algún conjunto de equivalentes, los añadimos a ese conjunto
                if prop1 in equivalent_set or prop2 in equivalent_set:
                    equivalent_set.add(prop1)
                    equivalent_set.add(prop2)
                    return
            # Si no se encontró ningún conjunto equivalente, creamos uno nuevo
            self.equivalents.append({prop1, prop2})
        except Exception as e:
            print(f"Error al agregar propiedades equivalentes ({prop1}, {prop2}): {e}")

    def get_equivalent_properties(self, predicate):
        """Obtiene todas las propiedades equivalentes a un predicado dado, considerando solo propiedades vinculadas por P1628."""
        try:
            for equivalent_set in self.equivalents:
                if predicate in equivalent_set:
                    return equivalent_set
            return {predicate}  # Si no se encuentra, solo devuelve la propiedad original
        except Exception as e:
            print(f"Error al obtener propiedades equivalentes para '{predicate}': {e}")
            return {predicate}

    def find(self, subject=None, predicate=None, obj=None):
        """Busca tripletas que coincidan con el patrón especificado."""
        try:
            matches = []
            # Recorrer los sujetos y sus predicados en la base de conocimiento
            for subj, preds in self.data.items():
                if subject and subj != subject:
                    continue
                for pred, objs in preds.items():
                    if (
                        predicate and pred != predicate
                    ):  # Solo comprobar si el predicado coincide
                        continue
                    for o in objs:
                        if obj and o != obj:  # Compara el objeto
                            continue
                        matches.append((subj, pred, o))
            return matches
        except Exception as e:
            print(f"Error al buscar tripletas con patrón ({subject}, {predicate}, {obj}): {e}")
            return []

    def show(self):
        """Muestra la base de conocimiento completa en un formato legible."""
        try:
            lineas = 0
            print("Base de Conocimiento:")
            for subject, predicates in self.data.items():
                print(f"  Sujeto: {subject}")
                for predicate, objects in predicates.items():
                    print(f"    Predicado: {predicate}")
                    for obj in objects:
                        print(f"      Objeto: {obj}")
                        lineas += 1  # Contamos cada tripleta como una línea

            # Mostrar equivalencias registradas
            print("\nPropiedades equivalentes registradas:")
            for equivalent_set in self.equivalents:
                print(f"  {', '.join(equivalent_set)}")
                lineas += 1  # Contamos cada conjunto de equivalentes como una línea

            print("\nNumero de lineas guardadas:", lineas)
        except Exception as e:
            print(f"Error al mostrar la base de conocimiento: {e}")
