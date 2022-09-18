#include<vector>
#include<algorithm>
using namespace std;

vector<vector<int>> merge(vector<vector<int>> &intervals)
{
    vector<vector<int>> res;
    
    sort(intervals.begin(), intervals.end(), [](const vector<int> &a, const vector<int> &b)
         { return a[0] < b[0]; });
    int l = intervals[0][0];
    int r = intervals[0][1];
    for (int i = 1; i < intervals.size(); i++)
    {
        if(intervals[i][0]<=r)
        {
            r = max(r, intervals[i][1]);
        }

        else
        {
            
            res.push_back({l,r});

            l = intervals[i][0];
            r = intervals[i][1];
        }
    }
    res.push_back({l, r});

    return res;
}