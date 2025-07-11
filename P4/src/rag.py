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


def retrieve_relevant_context(query, knowledge_base):
    """
    Recupera información relevante del conocimiento basado en la consulta.
    """
    # Reemplazar excepciones como Dr., Ing., Prof.
    query = re.sub(r"\b(dr|ing|prof)\.(?=\s)", r"\1", query)

    # Dividir la consulta en palabras y eliminar las stopwords
    query_words = [word for word in query.lower().split() if word not in STOPWORDS]

    relevant_context = []
    # Recorremos cada palabra clave de la consulta
    for word in query_words:
        # Si la palabra clave está en el diccionario knowledge_base
        if word in knowledge_base:
            for sentence in knowledge_base[word]:
                # Añadir la frase solo si no está ya en relevant_context
                if sentence not in relevant_context:
                    relevant_context.append(sentence)

    # Devolver las frases relevantes unidas por saltos de línea o un mensaje si no se encuentra información
    return (
        "\n\n".join(relevant_context)
        if relevant_context
        else "❌ No relevant information"
    )
