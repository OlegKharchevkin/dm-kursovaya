import argparse
import re
from graph import Graph
from hamiltonian_cycles import hamiltonian_cycle, color_cycle, del_ribs_not_in_cycle, clear_graph

true = ('t', 'true', '1', 'y', 'yes', 'д', 'да')
false = ('f', 'false', '0', 'n', 'no', 'н', 'нет')
colors = ("green",
          "red",
          "blue",
          "cyan",
          "pink",
          "yellow",
          "white",
          "black",
          "dark-green",
          "dark-red ",
          "dark-blue",
          "dark-cyan",
          "dark-pink",
          "dark-yellow")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    args = parser.parse_args()
    file = args.file
    graph = Graph()
    with open(file) as f:
        graph.read(f)
    text = graph.get_text()
    del_ribs = False
    color = colors[0]
    index = 0
    clear_color = colors[2]
    clear = False
    for line in text.splitlines():
        words = re.split(r'\s*=\s*', line)
        if len(words) == 2:
            match words[0]:
                case "del_ribs":
                    if words[1] in true or words[1] in false:
                        del_ribs = words[1] in true
                case "color":
                    if is_color(words[1]):
                        color = words[1]
                case "index":
                    if words[1].isdigit():
                        index = int(words[1])
                case "clear_color":
                    if is_color(words[1]):
                        clear_color = words[1]
                case "clear":
                    if words[1] in true or words[1] in false:
                        clear = words[1] in true
                case _:
                    pass
    if clear:
        clear_graph(graph, clear_color)
    cycle = hamiltonian_cycle(graph, index)
    if del_ribs:
        del_ribs_not_in_cycle(graph, cycle)
    color_cycle(graph, cycle, color)
    with open(file, 'w') as f:
        graph.write(f)
    return


def is_color(color: str) -> bool:
    if color in colors:
        return True
    if re.match(r'#[0-9a-fA-F]{6}', color):
        return True
    return False


if __name__ == "__main__":
    main()
