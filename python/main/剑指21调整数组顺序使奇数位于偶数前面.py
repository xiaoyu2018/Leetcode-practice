
def exchange(nums: list) -> list:
    i,j=0,len(nums)-1

    while(i<j):

        while(True):
            if(i<j and nums[i]%2==1):
                i+=1
            else:
                break
        
        while(True):
            if(i<j and nums[j]%2==0):
                j-=1
            else:
                break
        
        if(i<j):
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
    
    return nums

print(exchange([1,2,1,1]))