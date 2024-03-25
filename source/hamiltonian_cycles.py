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


def color_cycle(graph: Graph, cycle: list[int], rib_color: str) -> None:
    for i in ribs_from_cycle(cycle):
        graph.set_rib_color(i[0], i[1], rib_color)


def del_ribs_not_in_cycle(graph: Graph, cycle: list[int]) -> None:
    ribs = list(ribs_from_cycle(cycle))
    for rib in graph.get_ribs():
        if rib not in ribs:
            graph.delete_rib(rib[0], rib[1])


def ribs_from_cycle(cycle: list[int]):
    for i in range(len(cycle)):
        yield cycle[i - 1], cycle[i]
