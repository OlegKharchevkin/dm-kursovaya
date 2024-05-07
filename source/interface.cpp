#include "hamiltonianCycles.hpp"
#include "path.hpp"
#include "graph.hpp"
#ifdef __cplusplus
extern "C"
{
#endif
    Path *getHamiltonianCycles(int *matrix, int size, int index)
    {
        Graph graph(matrix, size);
        Path *path = new Path;
        DFS(*path, graph, 0, index);
        return path;
    }

    int pop(Path *path)
    {
        return path->pop();
    }
    int size(Path *path)
    {
        return path->getSize();
    }
#ifdef __cplusplus
}
#endif