import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo(G):
    """Dibuja el grafo con estilos personalizados de arista."""
    if G is None or len(G.nodes) == 0:
        raise ValueError("El grafo está vacío y no se puede dibujar.")

    try:
        pos = nx.spring_layout(G, k=1.5, iterations=50)
        edge_labels = nx.get_edge_attributes(G, "label")

        plt.figure(figsize=(10, 10))  # Tamaño de la figura
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=3000,
            node_color="skyblue",
            font_size=10,
            font_weight="bold",
            arrows=True,
        )

        solid_edges = [
            (u, v) for u, v, d in G.edges(data=True) if d.get("style") == "solid"
        ]
        dotted_edges = [
            (u, v) for u, v, d in G.edges(data=True) if d.get("style") == "dotted"
        ]

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=solid_edges,
            edge_color="green",
            style="solid",
            arrowstyle="->",
        )
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=dotted_edges,
            edge_color="blue",
            style="dotted",
            arrowstyle="->",
        )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        plt.savefig("graph.png", format="PNG", dpi=300)  # Guardar la imagen
        print("Grafo guardado como 'graph.png'.")
        plt.show()
    except Exception as e:
        print(f"Error al dibujar o guardar el grafo: {e}")
