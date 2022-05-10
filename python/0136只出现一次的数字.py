a=[4,1,2,1,2]


def singleNumber1(nums:list):
    d=dict()
    for i in nums:
        if(i not in d.keys()):
            d[i]=1
        else:
            d[i]+=1
    
    for i in d.keys():
        if(d[i]==1):
            return i

def singleNumber2(nums:list):
    s=set(nums)
    return sum(s)*2-sum(nums)

# 异或的交换律
def singleNumber3(nums:list):
    res=0
    for i in nums:
        res^=i
    
    return res

