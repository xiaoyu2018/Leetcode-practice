nums=[5,4,-1,7,8]

def maxSubArrray(nums):
    if(len(nums)==1):
        return nums[0]
    
    temp=nums[0]
    res=nums[0]
    
    for i in nums[1:]:
        # 计算以nums[i]结尾的最大连续子串和
        temp=max(temp+i,i)
        
        res=max(temp,res)
    
    return res


print(maxSubArrray(nums))
    