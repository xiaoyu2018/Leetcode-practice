#include<string>

using namespace std;

bool isAnagram(string s, string t)
{
    int memo[26] = {0};

    for(char i : s)
        ++memo[i - 97];
    for(char i : t)
        --memo[i - 97];

    for (int i = 0;i<26;++i)
    {
        if(memo[i])
            return false;
    }

    return true;
}

int main()
{
    
}