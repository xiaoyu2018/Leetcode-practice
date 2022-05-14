#include<vector>
#include<stdio.h>
using namespace std;

int minSubArrayLen(int target, vector<int> &nums)
{
    int nums_len = nums.size();
    int res = nums_len+ 1;
    int s = 0;
    int j = -1;
    for (int i = 0; i < nums_len; ++i)
    {
        s += nums[i];

        while(s>=target)
        {
            s -= nums[++j];

            res = res <= (i - j + 1) ? res : (i - j + 1);
        }
    }

    return res <nums_len +1 ? res : 0;
}

int main()
{
    vector<int> nums = {2,
                        3,
                        1,
                        2,
                        4,
                        3};
    printf("%d", minSubArrayLen(111, nums));
}