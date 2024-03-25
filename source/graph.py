from io import TextIOWrapper
from graphoid_parser import G_parser


class Graph:
    def __init__(self, size: int, matrix: list[list[int]], tags: dict) -> None:
        self.size = size
        self.matrix = matrix
        self.tags = tags

    def __init__(self, f: TextIOWrapper) -> None:
        parser = G_parser(f)
        self.size = parser.get_size()
        self.matrix = parser.get_matrix()
        self.tags = parser.get_tags()
