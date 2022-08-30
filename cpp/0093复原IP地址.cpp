#include<vector>
#include<string>
#include<iostream>
using namespace std;

vector<string> temp;
vector<string> res;

bool IsValid(string& s)
{
    if (s[0] == '0' and s.size() > 1)
        return false;
    if(s.size()<1||s.size()>3)
        return false;
    if (stoi(s) > 255)
        return false;
    return true;
}


void BackTracking(string &s,int start=0)
{
    if(temp.size()==4)
    {
        string ss;
        for(string s:temp)
        {
            
            ss.append(s + ".");
        }
        if(ss.size()==s.size()+4)
        {
            
            ss.pop_back();
            res.push_back(ss);
            return;
        }
    }

    for (int i = start;i<s.size();++i)
    {
        string ss = s.substr(start, i - start + 1);
        if (IsValid(ss))
        {
            // cout << 1;
            temp.push_back(ss);
            BackTracking(s,i + 1);
            temp.pop_back();
        }
    }
}

vector<string> restoreIpAddresses(string s)
{

    BackTracking(s);
    return res;
}

int main()
{
    restoreIpAddresses("25525511135");

    for (string s :res)
    {
        cout << s;
    }
        
}