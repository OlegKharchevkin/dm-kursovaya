from io import TextIOWrapper


class G_parser():
    def __init__(self, f: TextIOWrapper) -> None:
        self.__read_size(f)
        self.__read_matrix(f)
        self.__read_tags(f)

    def __read_size(self, f: TextIOWrapper) -> None:
        self.__size = int(f.readline())

    def __read_matrix(self, f: TextIOWrapper) -> None:
        self.__matrix = []
        for _ in range(self.__size):
            self.__matrix.append(list(map(int, f.readline().split())))

    def __read_tags(self, f: TextIOWrapper) -> None:
        self.__tags = {}
        tag = ""
        for line in f.readlines():
            if line.startswith("<"):
                tag = line.strip().replace("<", "").replace(">", "")
                match tag:
                    case "Text":
                        self.__tags[tag] = ""
                    case _:
                        self.__tags[tag] = {}
            else:
                if line.strip() == "":
                    continue
                match tag:
                    case "Text":
                        self.__tags[tag] += line
                    case "Vertex_Colors":
                        index, color = line.split()
                        self.__tags[tag][int(index)] = color
                    case "Positions":
                        index, x, y = map(int, line.split())
                        self.__tags[tag][index] = (x, y)
                    case "Rib_Colors":
                        start, end, color = line.split()
                        self.__tags[tag][(int(start), int(end))] = color
                    case _:
                        pass
        if "Text" not in self.__tags:
            self.__tags["Text"] = ""
        if "Vertex_Colors" not in self.__tags:
            self.__tags["Vertex_Colors"] = {}
        if "Positions" not in self.__tags:
            self.__tags["Positions"] = {}
        if "Rib_Colors" not in self.__tags:
            self.__tags["Rib_Colors"] = {}

    def get_size(self) -> int:
        return self.__size

    def get_matrix(self) -> list[list[int]]:
        return self.__matrix

    def get_tags(self) -> dict:
        return self.__tags


class G_writer():
    def __init__(self, f: TextIOWrapper, size: int, matrix: list[list[int]], tags: dict) -> None:
        self.__f = f
        self.__size = size
        self.__matrix = matrix
        self.__tags = tags

    def __write_size(self) -> None:
        self.__f.write(f"{self.__size}\n")

    def __write_matrix(self) -> None:
        for row in self.__matrix:
            self.__f.write(" ".join(map(str, row)) + "\n")

    def __write_tags(self) -> None:
        for tag in self.__tags:
            if len(self.__tags[tag]) != 0:
                self.__f.write(f"<{tag}>\n")
                match tag:
                    case "Text":
                        self.__f.write(self.__tags[tag])
                    case "Vertex_Colors":
                        for index, color in self.__tags[tag].items():
                            self.__f.write(f"{index} {color}\n")
                    case "Positions":
                        for index, position in self.__tags[tag].items():
                            self.__f.write(
                                f"{index} {position[0]} {position[1]}\n")
                    case "Rib_Colors":
                        for (start, end), color in self.__tags[tag].items():
                            self.__f.write(f"{start} {end} {color}\n")
                    case _:
                        pass

    def write(self) -> None:
        self.__write_size()
        self.__write_matrix()
        self.__write_tags()
