nums = [-1,0,3,5,9,12]
target = 9

def serch(nums:list,target:int):

    left=0
    right=len(nums)-1

    while(left<=right):
        mid=(left+right)>>1
        if(nums[mid]>target):
            right=mid-1
        elif(nums[mid]<target):
            left=mid+1
        else:
            return mid
    return -1

