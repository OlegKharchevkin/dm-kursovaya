#include "graph.hpp"
#include "path.hpp"

void DFS(Path &path, Graph graph, int vertex, int &index)
{
    path.add(vertex);
    if (path.getSize() == graph.getSize() && graph.isConnected(vertex, 0))
    {
        if (index != 0)
            path.pop();
        index -= 1;
        return;
    }
    for (int i = 0; i < graph.getSize(); i++)
        if (graph.isConnected(vertex, i) && !path.isInPath(i))
        {
            DFS(path, graph, i, index);
            if (path.getSize() == graph.getSize() && index == -1)
                return;
        }
    path.pop();
}