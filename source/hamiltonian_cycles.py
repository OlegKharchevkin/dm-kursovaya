from graph import Graph


def DFS_hamiltonian(path: "list[int]", graph: Graph, vertex: int, index: int) -> int:
    path.append(vertex)
    if len(path) == graph.get_size() and graph.is_connected(vertex, path[0]):
        if index != 0:
            path.pop()
        return index - 1

    for i in graph.get_vertices():
        if graph.is_connected(vertex, i) and i not in path:
            pass
            index = DFS_hamiltonian(path, graph, i, index)
            if len(path) == graph.get_size() and index == -1:
                return -1
    path.pop()
    return index


def hamiltonian_cycle(graph: Graph, index: int) -> "list[int]":
    cycle = []
    DFS_hamiltonian(cycle, graph, 0, index)
    return cycle


def color_cycle(graph: Graph, cycle: "list[int]", rib_color: str) -> None:
    nonoriented = graph.is_nonoriented()
    for i in ribs_from_cycle(cycle):
        graph.set_rib_color(i[0], i[1], rib_color)
        if nonoriented:
            graph.set_rib_color(i[1], i[0], rib_color)


def del_ribs_not_in_cycle(graph: Graph, cycle: "list[int]") -> None:
    nonoriented = graph.is_nonoriented()
    ribs = list(ribs_from_cycle(cycle))
    for rib in graph.get_ribs():
        if rib not in ribs:
            graph.delete_rib(rib[0], rib[1])
            if nonoriented and rib[::-1] not in ribs:
                graph.delete_rib(rib[1], rib[0])


def ribs_from_cycle(cycle: "list[int]"):
    for i in range(len(cycle)):
        yield cycle[i - 1], cycle[i]


def clear_graph(graph: Graph, color: str) -> None:
    for i in graph.get_ribs():
        graph.set_rib_color(i[0], i[1], color)
