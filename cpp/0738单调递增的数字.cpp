#include<vector>
#include<string>

using namespace std;

int monotoneIncreasingDigits(int n)
{
    string s = to_string(n);
    int len = s.size();
    int flag = s.size();
    for (int i = len - 1; i > 0; i--)
    {
        if(s[i-1]>s[i])
        {
            flag = i;
            s[i - 1]--;
        }
    }

    for (int i = flag; i < len; i++)
    {
        s[i] = '9';
    }

    return stoi(s);
}