nums = [3,2,2,3]
val = 3

def rm():
    slow=fast=0

    while(fast<len(nums)):
        if(nums[fast]!=val):
            nums[slow]=nums[fast]
            slow+=1
        fast+=1
    
    return slow

print(rm())
print(nums)