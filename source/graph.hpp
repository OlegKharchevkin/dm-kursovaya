#pragma once
class Graph
{
private:
    int *matrix;
    int size;

public:
    Graph(int *matrix, int size);
    bool isConnected(int start, int end);
    int getLength(int start, int end);
    int getSize();
    void addVertex();
    void addRib(int start, int end, int length = 1);
    void delVertex(int index);
    void delRib(int start, int end);
};
