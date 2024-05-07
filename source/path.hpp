#pragma once
struct NodePath;
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