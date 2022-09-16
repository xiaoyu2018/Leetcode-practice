#include<vector>
#include<algorithm>

using namespace std;
//记录非交叉区间的个数，最后用总区间个数减去非交叉区间的个数

//要按右区间从小到大排序，因为右区间越小，留余越大
static bool Cmp(const vector<int>& v1,const vector<int>& v2)
{
    return v1[1] < v2[1];
}

int eraseOverlapIntervals(vector<vector<int>> &intervals)
{
    sort(intervals.begin(), intervals.end(), Cmp);
    
    if(!intervals.size())
        return 0;

    int r = intervals[0][1];
    int count = 1;

    for (int i = 1; i < intervals.size(); i++)
    {
        if(intervals[i][0] >= r)
        {
            r = intervals[i][1];
            count++;
        }
        
    }

    return intervals.size() - count;
}