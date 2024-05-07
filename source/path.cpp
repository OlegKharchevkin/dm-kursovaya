struct NodePath
{
    int data;
    NodePath *next;
    NodePath(int data = 0, NodePath *next = nullptr) : data(data), next(next) {}
};
class Path
{
private:
    NodePath *head;
    int size = 0;

public:
    Path();
    ~Path();
    bool isEmpty();
    int getSize();
    void add(int data);
    int pop();
    int top();
    bool isInPath(int data);
};

Path::Path() : head(nullptr) {}

Path::~Path()
{
    NodePath *current = head;
    while (current != nullptr)
    {
        NodePath *next = current->next;
        delete current;
        current = next;
    }
}

bool Path::isEmpty()
{
    return head == nullptr;
}

int Path::getSize()
{
    return size;
}

void Path::add(int data)
{
    NodePath *newNode = new NodePath(data, head);
    head = newNode;
    size++;
}

int Path::pop()
{
    if (head != nullptr)
    {
        int data = head->data;
        NodePath *temp = head;
        head = head->next;
        delete temp;
        size--;
        return data;
    }
    return -1;
}

int Path::top()
{
    if (head != nullptr)
        return head->data;
    return -1;
}

bool Path::isInPath(int data)
{
    NodePath *current = head;
    while (current != nullptr)
    {
        if (current->data == data)
            return true;
        current = current->next;
    }
    return false;
}