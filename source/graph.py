from io import TextIOWrapper
import numpy as np


class Graph:
    @classmethod
    def from_numpy(cls, matrix: "np.ndarray[np.int32]" = [], tags: dict = {}) -> None:
        self = cls()
        self.__size = matrix.shape[0]
        self.__matrix = matrix.astype(np.int32)
        self.__tags = tags

    @classmethod
    def from_list(cls, matrix: "list[list[int]]" = [], tags: dict = {}) -> None:
        self = cls()
        self.__size = len(matrix)
        self.__matrix = np.array(matrix, dtype=np.int32)
        self.__tags = tags
        return self

    @classmethod
    def form_file(cls, f: TextIOWrapper) -> None:
        self = cls()
        self.__read_size(f)
        self.__read_matrix(f)
        self.__read_tags(f)
        return self

    def __init__(self) -> None:
        self.__size = 0
        self.__matrix = np.array([], dtype=np.int32)
        self.__tags = {}

    def write(self, f: TextIOWrapper) -> None:
        self.__write_size(f)
        self.__write_matrix(f)
        self.__write_tags(f)

    def set_vertex_color(self, index: int, color: str) -> None:
        self.__tags["Vertex_Colors"][index] = color

    def set_rib_color(self, start: int, end: int, color: str) -> None:
        self.__tags["Rib_Colors"][(start, end)] = color

    @property
    def is_nonoriented(self) -> bool:
        return (self.__matrix == self.__matrix.T).all()

    def add_rib(self, start: int, end: int, length: int = 1, color: str = "") -> None:
        self.__matrix[start][end] = length
        if color != "":
            self.set_rib_color(start, end, color)

    def add_vertex(self, coords: "tuple[int, int]" = None, color: str = "") -> None:
        new_matrix = np.zeros(
            (self.__size + 1, self.__size + 1), dtype=np.int32)
        new_matrix[:self.__size, :self.__size] = self.__matrix
        self.__matrix = new_matrix
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
        new_matrix = np.zeros(
            (self.__size - 1, self.__size - 1), dtype=np.int32)
        new_matrix[:index, :index] = self.__matrix[:index, :index]
        new_matrix[:index, index:] = self.__matrix[:index, index + 1:]
        new_matrix[index:, :index] = self.__matrix[index + 1:, :index]
        new_matrix[index:, index:] = self.__matrix[index + 1:, index + 1:]
        self.__matrix = new_matrix
        if index in self.__tags["Positions"]:
            self.__tags["Positions"].pop(index)
        if index in self.__tags["Vertex_Colors"]:
            self.__tags["Vertex_Colors"].pop(index)
        self.__tags["Rib_Colors"] = {k: v for k, v in self.__tags["Rib_Colors"].items(
        ) if k[0] != index and k[1] != index}

    @property
    def size(self) -> int:
        return self.__size

    def is_connected(self, start: int, end: int) -> bool:
        return self.__matrix[start][end] > 0

    @property
    def matrix(self) -> "np.ndarray":
        return self.__matrix.copy()

    @property
    def text(self) -> str:
        return self.__tags["Text"]

    def rib_color(self, start: int, end: int) -> str:
        if (start, end) not in self.__tags["Rib_Colors"]:
            return ""
        return self.__tags["Rib_Colors"][(start, end)]

    def rib_length(self, start: int, end: int) -> int:
        return int(self.__matrix[start][end])

    def vertex_color(self, index: int) -> str:
        if index not in self.__tags["Vertex_Colors"]:
            return ""
        return self.__tags["Vertex_Colors"][index]

    def position(self, index: int) -> "tuple[int, int]":
        if index not in self.__tags["Positions"]:
            return 0, 0
        return self.__tags["Positions"][index]

    @property
    def ribs(self):
        for start in range(self.__size):
            for end in range(self.__size):
                if self.is_connected(start, end):
                    yield start, end

    @property
    def vertices(self):
        for index in range(self.__size):
            yield index

    def __read_size(self, f: TextIOWrapper) -> None:
        self.__size = int(f.readline())

    def __read_matrix(self, f: TextIOWrapper) -> None:
        self.__matrix = np.zeros((self.__size, self.__size), dtype=np.int32)
        for i in range(self.__size):
            self.__matrix[i] = list(map(int, f.readline().split()))

    def __read_tags(self, f: TextIOWrapper) -> None:
        self.__tags = {}
        tag = ""
        for line in f.readlines():
            if line.startswith("<"):
                tag = line.strip().replace("<", "").replace(">", "")
                if tag == "Text":
                    self.__tags[tag] = ""
                else:
                    self.__tags[tag] = {}
            else:
                if line.strip() == "":
                    continue
                if tag == "Text":
                    self.__tags[tag] += line
                elif tag == "Vertex_Colors":
                    index, color = line.split()
                    self.__tags[tag][int(index)] = color
                elif tag == "Positions":
                    index, x, y = map(int, line.split())
                    self.__tags[tag][index] = (x, y)
                elif tag == "Rib_Colors":
                    start, end, color = line.split()
                    self.__tags[tag][(int(start), int(end))] = color

        if "Text" not in self.__tags:
            self.__tags["Text"] = ""
        if "Vertex_Colors" not in self.__tags:
            self.__tags["Vertex_Colors"] = {}
        if "Positions" not in self.__tags:
            self.__tags["Positions"] = {}
        if "Rib_Colors" not in self.__tags:
            self.__tags["Rib_Colors"] = {}

    def __write_size(self, f: TextIOWrapper) -> None:
        f.write(f"{self.__size}\n")

    def __write_matrix(self, f: TextIOWrapper) -> None:
        for i in range(self.__size):
            for j in range(self.__size):
                f.write(str(self.__matrix[i][j]) + " ")
            f.write("\n")

    def __write_tags(self, f: TextIOWrapper) -> None:
        for tag in self.__tags:
            if len(self.__tags[tag]) != 0:
                f.write(f"<{tag}>\n")
                if tag == "Text":
                    f.write(self.__tags[tag])
                elif tag == "Vertex_Colors":
                    for index, color in self.__tags[tag].items():
                        f.write(f"{index} {color}\n")
                elif tag == "Positions":
                    for index, position in self.__tags[tag].items():
                        f.write(
                            f"{index} {position[0]} {position[1]}\n")
                elif tag == "Rib_Colors":
                    for (start, end), color in self.__tags[tag].items():
                        f.write(f"{start} {end} {color}\n")
