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

Graph::Graph(int *matrix, int size)
{
    this->matrix = new int[size * size];
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            this->matrix[i * size + j] = matrix[i * size + j];
        }
    }
    this->size = size;
}

int Graph::getSize()
{
    return size;
}

bool Graph::isConnected(int start, int end)
{
    return matrix[start * size + end] != 0;
}

int Graph::getLength(int start, int end)
{
    return matrix[start * size + end];
}

void Graph::addRib(int start, int end, int length)
{
    matrix[start * size + end] = length;
}

void Graph::delRib(int start, int end)
{
    matrix[start * size + end] = 0;
}

void Graph::addVertex()
{
    int newSize = size + 1;
    int *newMatrix = new int[newSize * newSize];
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            newMatrix[i * newSize + j] = matrix[i * size + j];
        }
    }
    for (int i = 0; i <= size; i++)
    {
        newMatrix[i * newSize + size] = 0;
        newMatrix[size * newSize + i] = 0;
    }
    size = newSize;
    delete[] matrix;
    matrix = newMatrix;
}

void Graph::delVertex(int index)
{
    int newSize = size - 1;
    int *newMatrix = new int[newSize * newSize];
    for (int i = 0; i < index; i++)
    {
        for (int j = 0; j < index; j++)
            newMatrix[i * newSize + j] = matrix[i * size + j];

        for (int j = index + 1; j < size; j++)
            newMatrix[i * newSize + j - 1] = matrix[i * size + j];
    }
    for (int i = index + 1; i < size; i++)
    {
        for (int j = 0; j < index; j++)
            newMatrix[(i - 1) * newSize + j] = matrix[i * size + j];

        for (int j = index + 1; j < size; j++)
            newMatrix[(i - 1) * newSize + j - 1] = matrix[i * size + j];
    }
    size = newSize;
    delete[] matrix;
    matrix = newMatrix;
}