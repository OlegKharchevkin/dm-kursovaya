from io import TextIOWrapper


class G_parser():
    def __init__(self, f: TextIOWrapper) -> None:
        self.__read_size(f)
        self.__read_matrix(f)
        self.__read_tags(f)

    def __read_size(self, f: TextIOWrapper) -> None:
        self.size = int(f.readline())

    def __read_matrix(self, f: TextIOWrapper) -> None:
        self.matrix = []
        for _ in range(self.size):
            self.matrix.append(list(map(int, f.readline().split())))

    def __read_tags(self, f: TextIOWrapper) -> None:
        self.tags = {}
        tag = ""
        for line in f.readlines():
            if line.startswith("<"):
                tag = line.strip().replace("<", "").replace(">", "")
                match tag:
                    case "Text":
                        self.tags[tag] = ""
                    case _:
                        self.tags[tag] = {}
            else:
                match tag:
                    case "Text":
                        self.tags[tag] += line
                    case "Vertex_Colors":
                        index, color = line.split()
                        self.tags[tag][int(index)] = color
                    case "Positions":
                        index, x, y = map(int, line.split())
                        self.tags[tag][index] = (x, y)
                    case "Rib_Colors":
                        index1, index2, color = line.split()
                        self.tags[tag][(int(index1), int(index2))] = color
                    case _:
                        pass

    def get_size(self) -> int:
        return self.size

    def get_matrix(self) -> list[list[int]]:
        return self.matrix

    def get_tags(self) -> dict:
        return self.tags.copy()
