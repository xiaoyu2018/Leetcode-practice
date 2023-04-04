
# dp
def findLength(nums1: list, nums2: list) -> int:
    m=len(nums1)
    n=len(nums2)
    res=0
    dp=[[0]*n for _ in range(m)]

    for i in range(n):
        if(nums1[0]==nums2[i]):
            dp[0][i]=1
            res=1
    for i in range(m):
        if(nums2[0]==nums1[i]):
            dp[i][0]=1
            res=1

    for i in range(1,m):
        for j in range(1,n):
            if(nums1[i]==nums2[j]):
                dp[i][j]=dp[i-1][j-1]+1
                res=max(res,dp[i][j])
    
    return res

print(findLength([1,2,3,2,1],[0]))