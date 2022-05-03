test_nums=[3,3]
test_target=6
# 暴力
def TwoSum1(nums:list,target:int) -> list:
    nums_len=len(nums)
    for i in range(nums_len):
        for j in range(i+1,nums_len):
            if(nums[i]+nums[j]==target):
                return [i,j]

# 引入字典
def TwoSum2(nums:list,target:int) -> list:
    nums_len=len(nums)
    map={}

    for i in range(nums_len):
        j=map.get(target-nums[i])
        if(j!=None):
            return [i,j]
        map[nums[i]]=i


print(TwoSum2(test_nums,test_target))