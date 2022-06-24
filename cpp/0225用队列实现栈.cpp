#include<queue>

using namespace std;

class MyStack
{
public:
    queue<int> q;

    MyStack()
    {
    }

    void push(int x)
    {
        q.push(x);
    }

    int pop()
    {
        int len = q.size()-1;
        while(len--)
        {
            q.push(q.front());
            q.pop();
        }
        len = q.front();
        q.pop();
        return len;
    }

    int top()
    {
        int res = this->pop();
        q.push(res);
        return res;
    }

    bool empty()
    {
        return q.empty();
    }
};