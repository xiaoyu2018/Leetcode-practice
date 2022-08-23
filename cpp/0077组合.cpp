#include<iostream>
#include<vector>

using namespace std;

vector<vector<int>> res;
vector<int> temp;


void back_tracking(int s,int n,int k)
{
    if(k<1)
    {
        // 值传递
        res.push_back(temp);
        return;
    }

    for (;s<=n-k+1;++s)
    {
        temp.push_back(s);
        back_tracking(s + 1, n, k-1);
        temp.pop_back();
    }
}
vector<vector<int>> combine(int n, int k)
{
    back_tracking(1, n, k);

    return res;
}