# A semantic network stores concepts as nodes and relationships as edges.
network = {
    "Canary": {"is_a": "Bird"},
    "Bird": {"is_a": "Animal", "has": "Wings"},
    "Animal": {"needs": "Food"}
}

def show_relations(node):
    if node not in network:
        print("Concept not found.")
        return
    for relation, value in network[node].items():
        print(node, "--", relation, "-->", value)

show_relations("Bird")
