#include<iostream>
using namespace std;

// 反向遍历
int lengthOfLastWord(string s)
{
    int count = 0;
    int stop = s.find_last_not_of(' ');
    for (int i = stop; i > -1 && s[i] != ' '; --i, ++count)
        ;
    return count;
}

int main()
{
    string s = "aas";
    cout << lengthOfLastWord(s);
}
