#include <vector>
#include <iostream>
#include<map>
using namespace std;

class Solution
{
public:
    // 暴力
    vector<int> TwoSum1(vector<int> &nums, int target)
    {
        // 初始化大小为10的vector用res(10)
        // vector中的数据存在堆中，返回在栈中的变量，其指向的堆地址不会被清空
        vector<int> res;
        int len = nums.size();
        for (int i = 0;i<len;++i)
        {
            for (int j = i + 1; j < len; ++j)
            {
                if (nums[i] + nums[j] == target)
                {
                    // push_back会自动开辟新内存空间
                    res.push_back(i);
                    res.push_back(j);
                    return res;
                }
            }
        }
        return res;
    }

    // 引入字典
    vector<int> TwoSum2(vector<int> &nums,int target)
    {
        // 取map中不存在的key是会返回0，要对着一点进行处理
        map<int, int> temp_map;
        int len = nums.size();
        vector<int> res;
        for (int i = 0; i < len; ++i)
        {
            int value = temp_map[target - nums[i]];
            
            if(value)
            {
                res.push_back(i);
                res.push_back(value-1);
                return res;
            }

            temp_map[nums[i]] = i + 1;
        }

        return res;
    }
};


int main()
{
    vector<int> nums = {3,3};
    int target = 6;
    
    Solution *s = new Solution();
    auto res = s->TwoSum2(nums, target);
    cout << res[0] <<" "<< res[1]<<endl;

    
}