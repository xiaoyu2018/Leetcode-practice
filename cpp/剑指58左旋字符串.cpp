#include<string>

using namespace std;

void reverseByIndex(string &s,int l,int r)
{
    for (int i = 0;i<(r-l+1)>>1;++i)
    {
        s[l + i] ^= s[r - i];
        s[r - i] ^= s[l + i];
        s[l + i] ^= s[r - i];
    }
}
string reverseLeftWords1(string s, int n)
{
    reverseByIndex(s, 0, n-1);
    reverseByIndex(s, n, s.size()-1);
    reverseByIndex(s, 0, s.size()-1);

    return s;
}

string reverseLeftWords2(string s, int n)
{
    
    return s.substr(n,s.size()-n) + s.substr(0, n);
}