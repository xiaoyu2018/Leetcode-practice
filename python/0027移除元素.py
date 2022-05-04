
nums=[1,2,3,4]

# 首尾指针
def RemoveElement1(nums,val):
    if(not nums):
        return 0
    rear=len(nums)-1
    idx=0

    while(idx<=rear):
        if(nums[idx]==val and nums[rear]!=val):
            nums[idx],nums[rear]=nums[rear],nums[idx]

        if(nums[rear]==val):
            rear-=1
        if(nums[idx]!=val):
            idx+=1

    return rear+1

# 双指针（删除的元素会被覆盖）
def RemoveElement2(nums,val):
    res_idx=0
    for i in range(len(nums)):
        if(nums[i]!=val):
            nums[res_idx]=nums[i]
            res_idx+=1
    return res_idx
    
print(RemoveElement2(nums,1))
print(nums)