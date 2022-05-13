#include<vector>
#include<iostream>
#include<math.h>

using namespace std;

vector<int> sortedSquares(vector<int> &nums)
{
    int left = 0;
    int s = nums.size();
    int right = s-1;
    vector<int> res(s);
    --s;
    while (left <= right)
    {
        if(abs(nums[left])>abs(nums[right]))
        {
            res[s--] = nums[left] * nums[left];
            ++left;
        }
        else
        {
            res[s--] = nums[right] * nums[right];
            --right;
        }
    }

    return res;
}

int main()
{
    vector<int> nums = {1, 2, 3, 4};

    for(int i:sortedSquares(nums))
    {
        cout << i << endl;
    }
}