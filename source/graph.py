from io import TextIOWrapper
from graphoid_parser import G_parser, G_writer


class Graph:
    def __init__(self, size: int, matrix: list[list[int]], tags: dict) -> None:
        self.__size = size
        self.__matrix = matrix
        self.__tags = tags

    def __init__(self, f: TextIOWrapper) -> None:
        self.read(f)

    def __init__(self) -> None:
        self.__size = 0
        self.__matrix = []
        self.__tags = {}

    def read(self, f: TextIOWrapper) -> None:
        parser = G_parser(f)
        self.__size = parser.get_size()
        self.__matrix = parser.get_matrix()
        self.__tags = parser.get_tags()

    def write(self, f: TextIOWrapper) -> None:
        writer = G_writer(f, self.__size, self.__matrix, self.__tags)
        writer.write()

    def set_vertex_color(self, index: int, color: str) -> None:
        self.__tags["Vertex_Colors"][index] = color

    def set_rib_color(self, start: int, end: int, color: str) -> None:
        self.__tags["Rib_Colors"][(start, end)] = color

    def add_rib(self, start: int, end: int, length: int = 1, color: str = "") -> None:
        self.__matrix[start][end] = length
        if color != "":
            self.set_rib_color(start, end, color)

    def add_vertex(self, coords: tuple[int, int] = None, color: str = "") -> None:
        for row in self.__matrix:
            row.append(0)
        self.__matrix.append([0] * (self.__size + 1))
        self.__size += 1
        if coords is not None:
            self.__tags["Positions"][len(self.__tags["Positions"])] = coords
        if color != "":
            self.set_vertex_color(len(self.__tags["Vertex_Colors"]), color)

    def delete_rib(self, start: int, end: int) -> None:
        self.__matrix[start][end] = 0
        if (start, end) in self.__tags["Rib_Colors"]:
            self.__tags["Rib_Colors"].pop((start, end))

    def delete_vertex(self, index: int) -> None:
        self.__matrix.pop(index)
        for row in self.__matrix:
            row.pop(index)
        self.__size -= 1
        if index in self.__tags["Positions"]:
            self.__tags["Positions"].pop(index)
        if index in self.__tags["Vertex_Colors"]:
            self.__tags["Vertex_Colors"].pop(index)
        self.__tags["Rib_Colors"] = {k: v for k, v in self.__tags["Rib_Colors"].items(
        ) if k[0] != index and k[1] != index}

    def get_size(self) -> int:
        return self.__size

    def is_connected(self, start: int, end: int) -> bool:
        return self.__matrix[start][end] > 0

    def get_matrix(self) -> list[list[int]]:
        temp = [row.copy() for row in self.__matrix]
        return temp

    def get_text(self) -> str:
        return self.__tags["Text"]

    def get_rib_color(self, start: int, end: int) -> str:
        if (start, end) not in self.__tags["Rib_Colors"]:
            return ""
        return self.__tags["Rib_Colors"][(start, end)]

    def get_rib_length(self, start: int, end: int) -> int:
        return self.__matrix[start][end]

    def get_vertex_color(self, index: int) -> str:
        if index not in self.__tags["Vertex_Colors"]:
            return ""
        return self.__tags["Vertex_Colors"][index]

    def get_position(self, index: int) -> tuple[int, int]:
        if index not in self.__tags["Positions"]:
            return 0, 0
        return self.__tags["Positions"][index]

    def get_ribs(self):
        for start in range(self.__size):
            for end in range(self.__size):
                if self.is_connected(start, end):
                    yield start, end

    def get_vertices(self):
        for index in range(self.__size):
            yield index
