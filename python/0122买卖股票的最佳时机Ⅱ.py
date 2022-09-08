
# 贪心
def maxProfit(prices: list) -> int:
    res=0
    prev=prices[0]
    for i in prices[1:]:
        res=res+i-prev if i>prev else res
        prev=i

    return res 