nums=[1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6] 
n = 3

# 合并排序
def merge1(nums1: list, m: int, nums2: list, n: int):
    nums1[m:]=nums2
    nums1.sort()



# 双指针
def merge2(nums1: list, m: int, nums2: list, n: int):
    nums_temp=nums1[:m]
    i=j=k=0

    while(i<m and j<n):
        if(nums_temp[i]<nums2[j]):
            nums1[k]=nums_temp[i]
            i+=1
        else:
            nums1[k]=nums2[j]
            j+=1
        k+=1
    
    if(i==m):
        nums1[k:]=nums2[j:]
    if(j==n):
        nums1[k:]=nums_temp[i:]
    

merge2(nums,m,nums2,n)
print(nums)

