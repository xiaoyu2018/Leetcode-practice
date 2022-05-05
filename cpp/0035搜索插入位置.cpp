#include<iostream>
#include<vector>

using namespace std;

int SearchInsert(vector<int> nums,int target)
{
    if(nums.size()==0)
        return 0;

    int left = 0;
    int right = nums.size() - 1;
    int mid;
    while (left <= right)
    {
        mid = (left + right) >>1;
        if(nums[mid]==target)
            return mid;
        if(nums[mid]>target)
            right = mid - 1;
        else
            left = mid + 1;
    }

    return target <= nums[mid] ? mid : mid + 1;
}

int main()
{
    vector<int> nums = {1, 3, 5, 6};
    
    int target = 7;
    int a=SearchInsert(nums, target);
    cout << a;
}