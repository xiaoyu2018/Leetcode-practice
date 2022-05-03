#include<vector>
#include<iostream>

using namespace std;

// 快慢指针
int RemoveDuplicates(vector<int>& nums)
{
    int slow = 0;
    int fast = 1;
    while(fast<nums.size())
    {
        if(nums[slow]!=nums[fast])
            nums[++slow] = nums[fast];
        fast++;
    }

    return slow + 1;
}

int main()
{
    vector<int> v = {1, 1, 2, 2, 3};
    int a=RemoveDuplicates(v);
    cout << a <<endl;

    for (int i = 0; i < v.size(); ++i)
    {
        cout << v[i];
    }
}