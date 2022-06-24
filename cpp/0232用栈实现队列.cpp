#include<stack>
#include<vector>


using namespace std;

class MyQueue
{
private:
    stack<int> st1;
    stack<int> st2;

public:
    MyQueue()
    {
        
    }

    void push(int x)
    {
        st1.push(x);
    }

    int pop()
    {
        if(st2.empty())
        {
            while(!st1.empty())
            {
                st2.push(st1.top());
                st1.pop();
            }
        }
        int res = st2.top();
        st2.pop();
        return res;
    }

    int peek()
    {
        int res = this->pop();
        st2.push(res);
        return res;
    }

    bool empty()
    {
        return st1.empty() && st2.empty();
    }
};


int main()
{
    
}