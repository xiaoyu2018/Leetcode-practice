nums = [1]


def sortedSquares1(nums:list):
    
    return sorted([i*i for i in nums])

def sortedSquares2(nums:list):
    l=0
    r=len(nums)-1
    res=[]
    while(l<=r):
        if(abs(nums[l])<abs(nums[r])):
            res.append(nums[r]*nums[r])
            r-=1
        else:
            res.append(nums[l]*nums[l])
            l+=1
    
    return res[::-1]

print(sortedSquares2(nums))

