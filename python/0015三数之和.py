# 哈希
def threeSum(nums: list):
    memo=dict()
    res=[]
    for i,a in enumerate(nums):
        for j,b in enumerate(nums[i+1:],i+1):
            memo[a+b]=[i,j]
    
    for k,c in enumerate(nums):
        if(-c in memo.keys()):
            if(k not in memo[-c]):
                res.append([c,nums[memo[-c][0]],nums[memo[-c][1]]])
    
    
    for i,a in enumerate(res):
        for b in res[i+1:]:
            if(set(a)==set(b)):
                res.remove(b)
    return res

print(threeSum([-1,0,1,2,-1,-4]))


