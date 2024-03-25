import argparse
from graph import Graph
from hamiltonian_cycles import hamiltonian_cycle, color_cycle, del_ribs_not_in_cycle

true = ('t', 'true', '1', 'y', 'yes', 'д', 'да')
false = ('f', 'false', '0', 'n', 'no', 'н', 'нет')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    args = parser.parse_args()
    file = args.file
    graph = Graph(file)
    with open(file) as f:
        graph.read(f)
    text = graph.get_text()
    text_args = text.split()
    del_ribs = False
    color = "red"
    for arg in text_args:
        if arg in true:
            del_ribs = True
        elif arg not in false:
            color = arg
    cycle = hamiltonian_cycle(graph)
    if del_ribs:
        del_ribs_not_in_cycle(graph, cycle)
    color_cycle(graph, cycle, color)
    with open(file, 'w') as f:
        graph.write(f)
    return


if __name__ == "__main__":
    main()
