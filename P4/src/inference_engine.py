def chain_of_thought_prompt(query, context):
    """
    Genera un Chain of Thought (CoT) prompt que hace que el modelo reflexione en la consulta
    antes de dar su respuesta final.
    """
    # Step 1: Introducción del proceso reflexivo
    introduction = (
        "I will solve this query step by step by analyzing the problem carefully. "
        "I will think through each step before giving a final answer to ensure accuracy. "
        "This reasoning process will help organize my thoughts and improve the response.\n\n"
    )

    # Step 2: Presentación de la consulta y el contexto relevante
    presentation = f"User Query: {query}\nRelevant Context: {context}\n\n"

    # Step 3: Pasos detallados del razonamiento
    steps = (
        "Step 1: Identify key elements and entities mentioned in the query. "
        "What are the most important terms or topics here?\n"
        "Step 2: Cross-reference these elements with the provided context. "
        "Which parts of the context are directly relevant?\n"
        "Step 3: Analyze the relationships between the entities. "
        "For example, if a person and a course are mentioned, how are they connected?\n"
        "Step 4: Consider any gaps or ambiguities. If something is unclear, note it and make reasonable assumptions.\n"
        "Step 5: Formulate the final answer based on the reasoning above.\n\n"
    )

    # Step 4: Espacio para que el modelo genere su razonamiento y respuesta final
    final_prompt = (
        "Now, I will go through each step and write my reasoning before answering the query:\n\n"
        "Thought process:\n"
        "1. Identifying entities...\n"
        "2. Analyzing the context...\n"
        "3. Establishing relationships...\n"
        "4. Addressing ambiguities...\n"
        "5. Finalizing the answer...\n\n"
        "Answer:"
    )

    # Combinar todo en un único prompt
    return introduction + presentation + steps + final_prompt
