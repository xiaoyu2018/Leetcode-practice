#include<iostream>
#include<vector>
#include<stack>

using namespace std;

int GetResult(char opertator,int a,int b)
{
    int res;
    switch (opertator)
    {
        case '+':
            res = a + b;
            break;
        case '-':
            res = a - b;
            break;
        case '*':
            res = a * b;
            break;
        case '/':
            res = a / b;
            break;
        
    }
    return res;
}

int evalRPN(vector<string> &tokens)
{
    stack<int> st;
    int  a, b;
    for (string s : tokens)
    {
        if (s == "+" || s == "-" || s == "*" || s == "/")
        {
            a = st.top();
            st.pop();
            b = st.top();
            st.pop();
            st.push(GetResult(s[0], b, a));
        }
        else
            st.push(stoi(s));
    }

    return st.top();
}

int main()
{
    vector<string> t = {"2", "1", "+", "3", "*" };

    evalRPN(t);
}