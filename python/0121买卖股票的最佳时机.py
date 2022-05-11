prices=[7,1,5,3,6,4]

# 暴力超时
def maxProfit1( prices: list):
    profits=0

    size=len(prices)
    for i in range(size-1):

        for j in range(i+1,size):
            if(prices[i]>prices[j]):
                continue
            profits=max(profits,prices[j]-prices[i])
    return profits

# 动态规划
def maxProfit(prices:list):
    min_val=prices[0]
    res=0

    for i in prices[1:]:
        min_val=min(min_val,i)
        res=max(res,i-min_val)
    
    return res

print(maxProfit(prices))