
def maxProfit1(prices:list) -> int:
    if(not prices):
        return 0
    res=0
    dp=prices[0]

    for i in prices[1:]:
        res=max(res,i-dp)
        dp=min(dp,i)
    
    return res

