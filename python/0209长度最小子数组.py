target = 111
nums = [2,3,1,2,4,3]

# 暴力
def minSubArrayLen1(target: int, nums:list):
    # 以index结尾大于等于target的子数组长
    def _getLen(index , s=0):

        if(index<0):
            return 0
        
        s+=nums[index]
        
        if(s>=target):
            return 1
        
        ret=_getLen(index-1,s)

        return 0 if(not ret) else 1+ret 
        

    temp= [_getLen(i) for i in range(len(nums))]
    temp=[i for i in temp if i>0]
    if(not temp):
        return 0
    return min(temp)

# 暴力迭代
def minSubArrayLen2(target: int, nums:list):
    
    res=len(nums)+1
    for i in range(len(nums)):
        s=0
        for j in range(i,-1,-1):
            s+=nums[j]
            if(s>=target):
                res=min(res,i-j)
                break
    
    return res+1 if res<=len(nums) else 0


# 滑动窗口
def minSubArrayLen3(target: int, nums:list):
    size=len(nums)
    res=size+1
    s=0
    i=j=-1

    while(i<size):

        if(s>=target):
            j+=1
            s-=nums[j]
            res=min(i-j+1,res)
        else:
            i+=1
            if(i>=size):
                break
            s+=nums[i]  

    return 0 if res==size+1 else res
    


print(minSubArrayLen3(target,nums))