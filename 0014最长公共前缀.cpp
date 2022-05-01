#include<iostream>
#include<vector>
using namespace std;

// 暴力
string longestCommonPrefix1(vector<string> &strs)
{
    int size = strs.size();
    if (!size)
        return "";
    
    for (int i = 0;; ++i)
    {
        char ch = strs[0][i];
        for (int j = 1; j < size; ++j)
        {
            if(ch!=strs[j][i])
            {
                return strs[0].substr(0, i);
            }
        }

        if(strs[0][i]=='\0')
            return strs[0];
    }
}


// 分治
string _lcp(vector<string> &strs,int start, int end)
{
    if (start == end)
        return strs[start];
    if (start > end)
        return "";
    int mid = (start + end) / 2;
    string llcp = _lcp(strs, start, mid);
    string rlcp = _lcp(strs, mid+1, end);
    for (int i = 0;; ++i)
    {
        if(llcp[i]!=rlcp[i])
            return llcp.substr(0, i);
        
        if (llcp[i] == '\0')
            return llcp;
    }

}
string longestCommonPrefix2(vector<string> &strs)
{
    if(!strs.size())
        return "";
    return _lcp(strs, 0, strs.size()-1);
}

int main()
{
    vector<string> strs = {"flower", "flow", "flight"};

    cout<< longestCommonPrefix2(strs);
}