#include<vector>
#include<iostream>
using namespace std;

// 首尾指针
int RemoveElement1(vector<int>&nums,int val)
{
    int front = 0;
    int rear = nums.size()-1;
    int t;
    while (front <= rear)
    {
        if(nums[front]==val&&nums[rear]!=val)
        {
            t = nums[front];
            nums[front] = nums[rear];
            nums[rear] = t;
        }

        if (nums[rear] == val)
            --rear;
        if(nums[front]!=val)
            ++front;
    }
    return rear+1;
}

//双指针
int RemoveElement2(vector<int> &nums, int val)
{
    int res_idx = 0;
    int size = nums.size();

    for (int i = 0;i<size;++i)
    {
        if(nums[i]!=val)
            nums[res_idx++] = nums[i];
    }

    return res_idx;
}

int main()
{
    vector<int> nums = {1};
    int size = RemoveElement1(nums, 1);
    cout << size << endl;
    for (int i = 0; i < size; i++)
        cout << nums[i] << " ";
}