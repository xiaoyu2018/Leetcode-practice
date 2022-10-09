
def findMaxForm(strs: list, m: int, n: int) -> int:
    dp=[[0]*(n+1) for _ in range(m+1)]

    # 先遍历物品
    for s in strs:
        zeros=s.count('0')
        ones=s.count('1')
        # 再建立背包容量dp的二维数组，作为一个二维滚动数组
        for i in range(m,zeros-1,-1):
            for j in range(n,ones-1,-1):
                
                dp[i][j]=max(dp[i][j],dp[i-zeros][j-ones]+1)

    return dp[m][n]


if __name__ == '__main__':
    print(findMaxForm(["10","0001","111001","1","0"],5,3))