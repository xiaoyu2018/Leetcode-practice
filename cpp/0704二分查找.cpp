#include<vector>

using namespace std;

int serch(vector<int> &nums,int target)
{
    int left = 0;
    int right = nums.size() - 1;
    int mid;
    while (left <= right)
    {
        mid = (left + right) >> 1;

        if(nums[mid]==target)
            return mid;
        
        if(nums[mid]<target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}