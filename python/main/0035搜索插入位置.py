nums=[1, 3, 5, 6]
target=7

# 二分查找
def SearchInsert(nums,target):
    if(not nums):
        return 0
    left=0
    right=len(nums)-1

    while(left<=right):
        mid=(left+right)//2

        if(nums[mid]==target):
            return mid
        if(nums[mid]>target):
            right=mid-1
        else:
            left=mid+1
    
    return mid+1 if nums[mid]<target else mid


print(SearchInsert(nums,target))

    