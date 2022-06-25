#include <iostream>
#include<stack>
#include<map>
using namespace std;


// 栈
bool isValid(string s)
{
    map<char, char> m = {
        {'[',']'},
        {'{','}'},
        {'(',')'}
    };

    stack<char> st;

    if(m.find(s[0])==m.end())
        return false;
    
    st.push(s[0]);

    for (int i = 1;i<s.size();++i)
    {
        if (!(m.find(s[i]) == m.end()))
            st.push(s[i]);
        
        else
        {
            if(st.empty()||m[st.top()]!=s[i])
                return false;

            st.pop();
        }
    }

    return st.empty() ? true : false;
}

int main()
{
    string s = "(){}}{";
    cout << isValid(s);
}