from graph import Graph


def DFS_hamiltonian(path: list[int], graph: Graph, vertex: int) -> None:
    path.append(vertex)
    if len(path) == graph.get_size() and graph.is_connected(vertex, path[0]):
        return
    for i in graph.get_vertices():
        if graph.is_connected(vertex, i) and i not in path:
            DFS_hamiltonian(path, graph, i)
            if len(path) == graph.get_size():
                return
    path.pop()
    return


def hamiltonian_cycle(graph: Graph) -> list[int]:
    cycle = []
    DFS_hamiltonian(cycle, graph, 0)
    return cycle


def color_hamiltonian_cycle(graph: Graph, vertex_color: str, rib_color: str) -> None:
    cycle = hamiltonian_cycle(graph)
    for i in range(len(cycle)):
        graph.set_vertex_color(cycle[i], vertex_color)
        graph.set_rib_color(cycle[i - 1], cycle[i], rib_color)
