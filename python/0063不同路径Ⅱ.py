def uniquePathsWithObstacles(obstacleGrid: list) -> int:
    
    if(obstacleGrid[0][0]==1):
        return 0

    m=len(obstacleGrid)
    n=len(obstacleGrid[0])
    
    if(m==1 or n==1):
        return 0 if sum([sum(l) for l in obstacleGrid])>0\
        else 1

    dp=[[0]*n for _ in range(m)]

    for i in range(n):
        if(obstacleGrid[0][i]==1):
            break
        dp[0][i]=1
    for i in range(m):
        if(obstacleGrid[i][0]==1):
            break
        dp[i][0]=1

    for i in range(1,m):
        for j in range(1,n):
            if obstacleGrid[i][j]==1:
                continue
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    
    return dp[m-1][n-1]
    


print(uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))

