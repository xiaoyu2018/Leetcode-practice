nums=[1,2,3,4,1]

def containsDuplicate1(nums: list) -> bool:

    d=set()
    for i in nums:
        if(i in d):
            return True
        d.add(i)
    
    return False

def containsDuplicate2(nums: list) -> bool:
    return True if len(set(nums))<len(nums) else False

def containsDuplicate3(nums:list):
    d=dict()

    for i in nums:
        if(i in d.keys()):
            return True
        d[i]=1
    return False

print(containsDuplicate3(nums))