#include<string>
#include<iostream>

using namespace std;

string removeDuplicates(string s)
{
    string res;

    for(char c:s)
    {
        if (res.empty() or res.back() != c)
            res.push_back(c);
        else
            res.pop_back();
    }

    return res;
}

int main()
{
    cout << removeDuplicates("aaa");
}