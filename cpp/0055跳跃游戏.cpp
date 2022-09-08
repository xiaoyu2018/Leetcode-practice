#include<vector>

using namespace std;

bool canJump(vector<int> &nums)
{
    int cover = 1;
    for (int i = 0;i<cover;++i)
    {
        if(cover>=nums.size())
            return true;

        cover = max(cover, i + nums[i]+1);
    }

    return false;
}