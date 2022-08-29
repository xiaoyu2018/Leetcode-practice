#include<vector>
#include<iostream>

using namespace std;

vector<vector<string>> res;
vector<string> temp;


bool IsPalindrome(string &s,int left,int right)
{
    for (int i = 0; i <= ((right-left)>>1);++i)
        if(s[i+left]!=s[right-i])
            return false;
    return true;
}

void BackTracking(int start,string &s)
{
    if (start >= s.size())
    {
        res.push_back(temp);
        return;
    }

    for (int i = start;i<s.size();++i)
    {
        
        if (IsPalindrome(s, start, i))
        {
            
            temp.push_back(s.substr(start, i - start + 1));
            BackTracking(i+1, s);
            temp.pop_back();
        }

        else
            continue;
    }

}

vector<vector<string>> partition(string s)
{
    BackTracking(0, s);
    return res;
}


int main()
{
    partition("aab");
}