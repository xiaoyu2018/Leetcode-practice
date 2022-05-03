nums=[1,2,3,3,3]

# 快慢指针
def removeDuplicates(nums):
    if(not nums):
        return 0
    res_len=0
    
    for i in range(1,len(nums)):
        if(nums[res_len]!=nums[i]):
            res_len+=1
            nums[res_len]=nums[i]
    
    return res_len+1


print(removeDuplicates(nums))
print(nums)