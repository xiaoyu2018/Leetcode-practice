#include<vector>
#include<algorithm>

using namespace std;

static bool Cmp(const vector<int> &v1, const vector<int> &v2)
{
    return v1[0] < v2[0];
}

    int findMinArrowShots(vector<vector<int>> &points)
{

    sort(points.begin(), points.end(), Cmp);
    int res = 1;
    int r = points[0][1];

    for (int i = 1; i < points.size(); i++)
    {
        if(points[i][0]>r)
        {
            res++;
            r = points[i][1];
        }
        else if (points[i][1]<r)
        {
            r = points[i][1];
        }
    }

    return res;
}