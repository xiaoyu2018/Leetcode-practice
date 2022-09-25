
# 回溯（超时）
def uniquePaths1(m: int, n: int) ->int:
    res=0
    # if(m==n==1):
    #     return 0

    def _backTracking(m:int,n:int):
        nonlocal res
        
        # 走到指定位置
        if(m==n==0):
            res+=1
            return
        
        # 每层递归都选向右走还是向下走其中之一
        # 保证不走过头且通过回溯每条路都会选到
        if(m>0):
            _backTracking(m-1,n)
        
        if(n>0):
            _backTracking(m,n-1)
    
    # m*n只需要向左走m-1步，向下走n-1步
    _backTracking(m-1,n-1)
    return res

# 深搜（本质和回溯一样）
# 将向右走看成左子树，向下走看成右子树，叶子节点就是走到终点的情况
def uniquePaths2(m: int, n: int) ->int:
    # if(m==n==1):
    #     return 0
    
    def _dfs(m:int,n:int):
        if(m<0 or n<0):
            return 0
        if(m==n==0):
            return 1
        return _dfs(m-1,n)+_dfs(m,n-1)

    return _dfs(m-1,n-1)

# dp
# 1 dp[i][j]：表示从（0 ，0）出发，到(i, j) 有dp[i][j]条不同的路径。
# 2 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
# 3 dp[0][0] = 1
# 4 从左上到右下遍历即可
# 5
def uniquePaths3(m: int, n: int) ->int:
    
    dp=[[1]*n for _ in range(m)]
    
    for i in range(1,m):
        for j in range(1,n):
            
            dp[i][j]=dp[i - 1][j] + dp[i][j - 1]

    return dp[m-1][n-1]

print(uniquePaths3(3,7))

