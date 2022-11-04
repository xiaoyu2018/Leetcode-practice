
# 双指针
def findLengthOfLCIS(nums: list) -> int:
    l=0
    r=0
    res=0
    size=len(nums)

    while(r<size):
        r+=1
        res=max(res,r-l)
        if(r>=size):
            break
        if(nums[r]<=nums[r-1]):
            l=r

    return res

# dp
def findLengthOfLCIS1(nums: list) -> int:
    dp=1
    res=1
    for i in range(1,len(nums)):

        if(nums[i]>nums[i-1]):
            dp+=1
            res=max(res,dp)
        else:
            dp=1
    
    return res

print(findLengthOfLCIS( [] ))