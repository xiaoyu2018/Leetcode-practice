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

print(maxProfit2(prices))