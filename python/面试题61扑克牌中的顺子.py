
def isStraight(nums: list) -> bool:
    nums.sort()
    x=y=0

    for i in range(len(nums)-1):
        if(nums[i]==0):
            x+=1
        else:
            if(nums[i+1]==nums[i]):
                return False
            y+=nums[i+1]-nums[i]-1
        
    return x>=y