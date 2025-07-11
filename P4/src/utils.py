import os
from collections import defaultdict
import re

# Stopwords comunes en inglés
STOPWORDS = {
    "a",
    "an",
    "the",
    "and",
    "or",
    "but",
    "in",
    "on",
    "at",
    "by",
    "for",
    "with",
    "about",
    "as",
    "of",
    "to",
    "is",
    "are",
    "was",
    "were",
    "be",
    "being",
    "been",
    "this",
    "that",
    "it",
    "they",
    "we",
    "he",
    "she",
    "you",
    "I",
    "me",
    "him",
    "her",
    "them",
    "my",
    "your",
    "his",
    "its",
    "their",
    "our",
    "who",
    "whom",
    "which",
    "what",
}


def extraer_palabras_clave(sentence):
    """
    Extrae palabras significativas (sustantivos y palabras útiles) de una frase.
    Excluye stopwords.
    """
    words = re.findall(r"\b\w+\b", sentence)  # Encuentra todas las palabras
    meaningful_words = [word.lower() for word in words if word.lower() not in STOPWORDS]
    return meaningful_words


def load_knowledge_base(directory):
    """
    Carga todos los archivos .txt desde el directorio y construye un diccionario
    con palabras significativas como claves y frases asociadas como valores.
    """
    knowledge_base = defaultdict(list)  # defaultdict para evitar KeyError

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Leer el contenido del archivo
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        content = content.lower()

        # Reemplazar excepciones como Dr., Ing., Prof.
        text = re.sub(r"\b(dr|ing|prof)\.", r"\1<STOP>", content)

        # Dividir usando un punto seguido de espacio
        sentences = re.split(r"\.", text)

        # Restaurar los marcadores a su forma original
        sentences = [oracion.replace("<STOP>", ".") for oracion in sentences]

        for sentence in sentences:
            sentence = sentence.strip()  # Eliminar espacios extra
            if not sentence or "#" in sentence:
                continue

            # Extraer palabras significativas de la frase
            meaningful_words = extraer_palabras_clave(sentence)

            for word in meaningful_words:
                knowledge_base[word].append(sentence)  # Añadir la frase al diccionario

    return dict(
        knowledge_base
    )  # Convertir defaultdict a un diccionario normal si es necesario
