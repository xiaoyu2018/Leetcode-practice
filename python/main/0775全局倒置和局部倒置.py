
# 暴力，直接检查nums中是否存在非局部倒置的全局倒置
def isIdealPermutation(nums: list) -> bool:

    for i in range(len(nums)-2):
        for j in range(i+2,len(nums)):
            if(nums[i]>nums[j]):
                return False
    
    return True

# 进一步的，只需检验下标为i的元素是否大于i+1后元素中的最小值
# 而最小值可以递推，从而降低时间复杂度
def isIdealPermutation1(nums: list) -> bool:
    min_suf=nums[-1]

    for i in range(len(nums)-3,-1,-1):
        if(nums[i]>min_suf):
            return False
        min_suf=min(nums[i+1],min_suf)

    return True

print(isIdealPermutation1([1,0,2,3]))