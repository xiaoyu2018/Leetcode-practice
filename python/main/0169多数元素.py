

# 引入额外哈希表
def majorityElement1(nums: list):
    d=dict()

    for i in nums:
        if(i not in d.keys()):
            d[i]=1
        else:
            d[i]+=1
    
    for i in d.keys():
        if(d[i]>len(nums)//2):
            return i

# 排序取中
def majorityElement2(nums: list):
    nums.sort()
    return nums[len(nums)>>1]


# 分治
def majorityElement3(nums:list):
    
    def _getMajority(l,r):
        if(l==r):
            return nums[l]
        
        mid=(l+r)>>1
        lm=_getMajority(l,mid)
        rm=_getMajority(mid+1,r)

        if(lm==rm):
            return lm
        
        return lm if nums[l:r+1].count(lm)>nums[l:r+1].count(rm) else rm

    return _getMajority(0,len(nums)-1)

nums = [6,1,6]
print(majorityElement3(nums))