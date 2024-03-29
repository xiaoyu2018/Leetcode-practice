
def minDistance(word1: str, word2: str) -> int:
    m=len(word1)+1
    n=len(word2)+1

    dp=[[0]*n for _ in range(m)]

    # 初始化
    for i in range(1,m):
        dp[i][0]=i
    for i in range(1,n):
        dp[0][i]=i

    for i in range(1,m):
        for j in range(1,n):
            if(word1[i-1]==word2[j-1]):
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+2)
    
    return dp[-1][-1]