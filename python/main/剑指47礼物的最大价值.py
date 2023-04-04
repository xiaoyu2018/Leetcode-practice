
def maxValue(grid: list) -> int:
    
    m=len(grid)
    n=len(grid[0])
    
    if(m==0 or n==0):
        return 0
    
    dp=[[0]*n for _ in range(m)]
    dp[0][0]=grid[0][0]

    for i in range(1,n):
        dp[0][i]=dp[0][i-1]+grid[0][i]
    for i in range(1,m):
        dp[i][0]=dp[i-1][0]+grid[i][0]
    
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=grid[i][j]+max(dp[i-1][j],dp[i][j-1])
    print(dp)
    return max(dp[-1])

maxValue([
    [1,4,8,6,2,2,1,7],
    [4,7,3,1,4,5,5,1],
    [8,8,2,1,1,8,0,1],
    [8,9,2,9,8,0,8,9],
    [5,7,5,7,1,8,5,5],
    [7,0,9,4,5,6,5,6],
    [4,9,9,7,9,1,9,0]
          ])