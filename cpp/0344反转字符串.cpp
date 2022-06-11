#include<vector>
#include<stdio.h>

using namespace std;

void reverseString1(vector<char> &s)
{
    int len = s.size();
    vector<char> ss(len);

    for (int i = len - 1;i>=0;--i)
    {
        ss[i] = s[len - i - 1];
    }

    s = ss;
}

void reverseString2(vector<char> &s)
{
    int len = s.size();
    

    for (int i = 0,j=len-1;i<len>>1;++i,--j)
    {
        s[i] ^= s[j];
        s[j] ^= s[i];
        s[i] ^= s[j];
    }
}

int main()
{
    vector<char> s={'a','b','c'};

    reverseString2(s);

    for (int i = 0;i<s.size();++i)
    {
        printf("%c", s[i]);
    }
}