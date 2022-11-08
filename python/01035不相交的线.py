
# 相对顺序不变，最大相同元素数
def maxUncrossedLines(nums1: list, nums2: list) -> int:
    m=len(nums1)
    n=len(nums2)

    dp=[[0]*n for _ in range(m)]

    for i in range(m):
        if(nums2[0]==nums1[i]):
            for j in range(i,m):
                dp[j][0]=1
            break
    for i in range(n):
        if(nums1[0]==nums2[i]):
            for j in range(i,n):
                dp[0][j]=1
            break

    for i in range(1,m):
        for j in range(1,n):
            if(nums1[i]==nums2[j]):
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    return dp[-1][-1]