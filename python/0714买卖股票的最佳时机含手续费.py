
# 贪心
def maxProfit(prices:list, fee: int) -> int:
    # 在买入时计算上手续费，有一次买入了必然要有一次卖出，手续费不会计算错误
    buy=prices[0]+fee
    res=0

    for p in prices[1:]:
        
        # 有更低价格的买入机会
        if(buy>p+fee):
            buy=p+fee
        
        # 卖出有利润，但是有手续费要追求最大利润就假卖
        if(p>buy):
            res+=p-buy # 部分利润
            buy=p # 记录假卖出点，使得重新买入前的卖出不重复扣除手续费
    
    return res

# dp
# 0 持有股票状态
# 1 不持有股票状态
def maxProfit1(prices:list, fee: int) -> int:
    dp=[-prices[0],0]

    for price in prices:
        dp[0]=max(dp[0],dp[1]-price)
        dp[1]=max(dp[1],dp[0]+price-fee)
    
    return dp[-1]



print(maxProfit1([1,3,2,8,4,9],2))

