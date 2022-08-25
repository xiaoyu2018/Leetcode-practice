#include<vector>

using namespace std;

vector<vector<int>> res;
vector<int> temp;
int sum = 0;

void BackTracking(int s, int k, int n)
{
    if(sum>n)
        return;
    if (k < 1)
    {
        if(sum==n)
            res.push_back(temp);
        return;
    }

    for (int i = s;i<10;++i)
    {
        sum += i;
        temp.push_back(i);
        BackTracking(i + 1, k - 1, n);
        temp.pop_back();
        sum -= i;
    }
}

vector<vector<int>> CombinationSum3(int k,int n)
{
    BackTracking(1, k, n);
    return res;
}