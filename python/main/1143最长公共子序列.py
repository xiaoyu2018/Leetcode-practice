
# 动态规划
# dp[i][j]为text1中前i项和text2中前j项子串最长公共子序列
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m=len(text1)
    n=len(text2)

    dp=[[0]*n for _ in range(m)]

    for i in range(m):
        if(text2[0]==text1[i]):
            for j in range(i,m):
                dp[j][0]=1
            break
    
    for i in range(n):
        if(text2[i]==text1[0]):
            dp[0][i:]=[1]*(n-i)

    
    # 递推公式
    for i in range(1,m):
        for j in range(1,n):
            if(text1[i]==text2[j]):
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    
    return dp[-1][-1]

