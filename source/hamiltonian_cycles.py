from graph import Graph
from ctypes import *


clib = CDLL("libinterface.dll")


def hamiltonian_cycle(graph: Graph, index: int) -> "list[int]":
    size = graph.size
    matrix = graph.matrix.ctypes.data_as(c_int * size * size)
    ccycle = clib.getHamiltonianCycles(matrix, size, index)
    return [clib.pop(ccycle) for _ in range(clib.size(ccycle))]


def color_cycle(graph: Graph, cycle: "list[int]", rib_color: str) -> None:
    nonoriented = graph.is_nonoriented
    for i in ribs_from_cycle(cycle):
        graph.set_rib_color(*i, rib_color)
        if nonoriented:
            graph.set_rib_color(*i[::-1], rib_color)


def del_ribs_not_in_cycle(graph: Graph, cycle: "list[int]") -> None:
    nonoriented = graph.is_nonoriented
    ribs = list(ribs_from_cycle(cycle))
    for rib in graph.ribs():
        if rib not in ribs:
            graph.delete_rib(*rib)
            if nonoriented and rib[::-1] not in ribs:
                graph.delete_rib(*rib[::-1])


def ribs_from_cycle(cycle: "list[int]"):
    for i in range(len(cycle)):
        yield cycle[i - 1], cycle[i]


def clear_graph(graph: Graph, color: str) -> None:
    for i in graph.ribs:
        graph.set_rib_color(i[0], i[1], color)
