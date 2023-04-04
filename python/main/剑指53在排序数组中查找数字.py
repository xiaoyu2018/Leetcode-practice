
# 先二分再前后遍历
def search(nums: list, target: int) -> int:
    res=0
    l,r=0,len(nums)-1
    m=l+((r-l)>>1)

    while(l<=r):
        m=l+((r-l)>>1)
        if(nums[m]==target):
            break
        elif(nums[m]>target):
            r=m-1
        else:
            l=m+1
    
    temp=m+1
    while(m>=0 and nums[m]==target):
        res+=1
        m-=1
    while(temp<len(nums) and nums[temp]==target):
        res+=1
        temp+=1

    return res

print(search([1,1,3],1))