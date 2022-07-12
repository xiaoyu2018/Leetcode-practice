#include<vector>
#include<algorithm>
using namespace std;

int findContentChildren(vector<int> &g, vector<int> &s)
{
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());
    int count = 0;
    for (int i = g.size() - 1, j = s.size(); i >=0 &&j >=0 ; --i)
    {
        if(g[i]<=s[j])
        {
            ++count;
            --j;
        }
    }

    return count;
}