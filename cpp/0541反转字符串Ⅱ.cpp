#include<string>
#include<iostream>
#include<algorithm>
using namespace std;

string reverseStr(string s, int k)
{

    for (int i = 0;i<s.size();i+=2*k)
    {
        if(i+k>s.size())
        {
            reverse(s.begin() + i, s.end());
            break;
        }
        reverse(s.begin() + i, s.begin() + i + k);
    }

    return s;
}

int main()
{
    string s = "123";
    reverse(s.begin(), s.begin() + 4);
    cout << s;
}