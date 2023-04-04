
def twoSum(nums: list, target: int):

    memo=dict()
    memo[nums[0]]=0
    for i,e in enumerate(nums[1:],1):
        
        if(target-e in memo.keys()):
            return [i,memo[target-e]]
        
        memo[e]=i
    
