
def unequalTriplets(nums: list) -> int:
    size=len(nums)
    res=0
    for i in range(size):
        for j in range(i+1,size):
            for k in range(j+1,size):
                res+=(nums[i]!=nums[j] and nums[j]!=nums[k] and nums[i]!=nums[k])

    return res       

