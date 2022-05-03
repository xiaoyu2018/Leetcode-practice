#include<iostream>
#include<map>

using namespace std;

int RomanToInt(string s)
{
    map<char, int> r2i_map = {{'I' ,1},
                              {'V' , 5},
                              {'X' , 10},
                              {'L' , 50},
                              {'C' , 100},
                              {'D' ,500},
                              {'M' , 1000}};
    int res = 0;
    int count = 0;
    for (; s[count + 1] != '\0'; ++count)
    {
        int val = r2i_map[s[count]];
        if (val >= r2i_map[s[count + 1]])
            res += val;
        else
            res -= val;
    }
    res += r2i_map[s[count]];
    return res;
}

int main()
{
    string s = "III";
    printf("%d", RomanToInt(s));
}