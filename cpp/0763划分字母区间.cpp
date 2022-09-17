#include<vector>
#include<string>

using namespace std;

vector<int> partitionLabels(string s)
{
    vector<int> res;
    int count = 0;
    int memo[26] = {0};
    int furthest = -1;
    int idx;
    for (int i = 0; i < s.size(); i++)
    {
        idx = s[i] - 'a';
        if (i > memo[idx])
            memo[idx] = i;
    }

    for (int i = 0; i < s.size(); i++)
    {
        count++;
        idx = s[i] - 'a';
        furthest = max(furthest, memo[idx]);
        if (i == furthest)
        {
            res.push_back(count);
            count = 0;
        }
    }
    return res;
}