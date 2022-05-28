#include<string>
using namespace std;


bool canConstruct(string ransomNote, string magazine)
{
    int memo[26] = {0};

    for(char c :magazine)
    {
        ++memo[c - 'a'];
    }

    for(char c:ransomNote)
    {
        int a=--memo[c - 'a'];
        if(a<0)
            return false;
    }

    return true;
}