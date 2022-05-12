#include<vector>
#include<iostream>
#include<map>

using namespace std;

bool containsDuplicate(vector<int> &nums)
{
    map<int, int> m;

    for(int i :nums)
    {
        if(m[i]>0)
            return true;
        m[i] += 1;
    }
    return false;
}
int main()
{
    vector<int> nums = {1,1,2,2,3};
    cout << containsDuplicate(nums);
}