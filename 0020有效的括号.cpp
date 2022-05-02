#include <iostream>
#include <vector>
#include<stack>
#include<map>
using namespace std;


// 栈
bool isValid(string s)
{
    stack<char> st;
    map<char, char> brackets_map = {
        {']','['},
        {')','('},
        {'}','{'},
    };

    for (int i = 0; s[i] != '\0'; ++i)
    {
        if(s[i]=='('||s[i]=='['||s[i]=='{')
            st.push(s[i]);
        else
        {
            if(not st.size())
                return false;
            char top_val = st.top();
            st.pop();
            if(top_val!=brackets_map[s[i]])
                return false;
        }
    }

    return !st.size();
}

int main()
{
    string s = "";
    cout << isValid(s);
}