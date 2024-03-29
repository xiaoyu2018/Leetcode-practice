prices=[
        7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,5,3,6,47,1,5,3,6,4,
        1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,
        7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,5,3,6,47,1,5,3,6,4,
        1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,
        7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,5,3,6,47,1,5,3,6,4,
        1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,
        7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,5,3,6,47,1,5,3,6,4,
        1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,
        7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,5,3,6,47,1,5,3,6,4,
        1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,
        7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,5,3,6,47,1,5,3,6,4,
        1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,
        7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,5,3,6,47,1,5,3,6,4,
        1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,
        7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,5,3,6,47,1,5,3,6,4,
        1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,
        7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,5,3,6,47,1,5,3,6,4,
        1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,
        7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,5,3,6,47,1,5,3,6,4,
        1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,
        7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,5,3,6,47,1,5,3,6,4,
        1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,
        7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,5,3,6,47,1,5,3,6,4,
        1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,7,1,5,3,6,4,7,1,5,3,6,47,1,5,3,6,4,
        ]*1500

# 暴力
def maxProfit1( prices: list):
    # 找到第index天卖出能获取的最大利润
    def _getProf(index:int):
        if(not index):
            return 0
        
        min_price=min(prices[:index])
        return prices[index]-min_price
    
    return max([_getProf(i) for i in range(len(prices))])

# 记忆化
def maxProfit2( prices: list):
    
    memo=dict()
    # 找到第index天卖出能获取的最大利润
    def _getProf(index:int):
        
        if(not index):
            memo[0]=prices[0]
            return 0
        
        memo[index]=min(memo[index-1],prices[index])
        return prices[index]-memo[index]
    
    return max([_getProf(i) for i in range(len(prices))])

# 优化空间
def maxProfit3(prices:list):
    min_val=prices[0]
    res=0

    for i in prices[1:]:
        min_val=min(min_val,i)
        res=max(res,i-min_val)
    
    return res



def mp1(prices:list):
    memo=dict() #记录第i天及以后的最大值
    memo[len(prices)-1]=0
    def _gp(index:int):
        if(index<len(prices)-1):
            
            memo[index]=max(prices[index+1],memo[index+1])
            res=memo[index]-prices[index]
            return res if res>0 else 0
        return 0
   
    return max([_gp(i) for i in range(len(prices)-1,-1,-1)])


def mp2(prices:list):
    max_val=0
    res=0
    for i in prices[::-1]:
        res=max(res,max_val-i)
        max_val=max(i,max_val)

    return res

# 动态规划
def mp3(prices:list):
    # dp[i][0]，第i天持有股票的最小花费（也就是第i天及之前的最低股票价格）
    # dp[i][1]，第i天不持有股票的最大利润（也就是第i天及之前的卖出股票能得到最大利润）
    size=len(prices)
    dp=[[0,0]]*size
    dp[0][0]=-prices[0]
    dp[0][1]=0

    for i in range(1,size):
        dp[i][0]=max(dp[i-1][0],-prices[i])
        dp[i][1]=max(dp[i-1][1],prices[i]+dp[i-1][0])
    
    return dp[size-1][1]
print(mp3(prices))

