
def twoSum(nums: list, target: int) -> list:
    i,j=0,len(nums)-1

    while(i<j):
        s=nums[i]+nums[j]
        if(s==target):
            return [nums[i],nums[j]]
        if(s>target):
            j-=1
        else:
            i+=1
    
    return []