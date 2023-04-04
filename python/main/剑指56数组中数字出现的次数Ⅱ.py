
def singleNumber(nums: list) -> int:
    d=dict()

    for i in nums:
        d[i]=d.get(i,0)+1
    
    for k in d.keys():
        if(d[k]==1):
            return k
    return -1