
# 超时
def lastRemaining( n: int, m: int) -> int:
    nums=[i for i in range(n)]
    c1,c2=0,1
    i=0
    while(c1<n-1):
        if(nums[i]!=-1):
            if(c2==m):
                c2=0
                nums[i]=-1
                c1+=1
            c2+=1
        i=(i+1)%n
        
    print(nums)
    
    for n in nums:
        if(n!=-1):
            return n

print(lastRemaining(100000,100000))