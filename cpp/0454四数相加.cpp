#include<unordered_map>
#include<vector>
using namespace std;

int fourSumCount(vector<int> &nums1, vector<int> &nums2, vector<int> &nums3, vector<int> &nums4)
{
    int count;
    unordered_map<int, int> memo;
    for (int i : nums1)
    {
        for(int j:nums2)
        {
            ++memo[i + j];
        }
    }

    for(int i:nums3)
    {
        for(int j: nums4)
        {
            if(memo.find(-i-j)!=memo.end())
                count+=memo[-i-j];
        }
    }

    return count;
}
