#include<vector>
#include<iostream>

using namespace std;
// 暴力
bool IsPalindrome1(int x)
{
    if(x<0)
        return false;
    vector<int> nums;

    while (x>0)
    {
        nums.push_back(x%10);
        x /= 10;
    }
    int size = nums.size();

    for (int i = 0;i<size/2;++i)
    {
        if(nums[i]!=nums[size-i-1])
            return false;
    }
    return true;
}

// 逆置一半
bool IsPalindrome2(int x)
{
    if (x==0)
        return true;
    if (x < 0 || (x % 10 == 0))
        return false;
    int re_num = 0;

    // 仅拆分数字的一般保存到另一变量中
    while(x>re_num)
    {
        re_num = re_num * 10 + x % 10;
        x /= 10;
    }
    // 当原数字为奇数时直接去掉中间数字
    return x == re_num || x == re_num / 10;
}

int main()
{
    cout << IsPalindrome1(121) <<endl;
    cout << IsPalindrome2(121) << endl;
}