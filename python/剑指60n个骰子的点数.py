# 超时
def dicesProbability(n: int) -> list:
    memo={i:0 for i in range(n,6*n+1)}

    def _back_tracking(n:int ,s:int):

        if(n==0):
            memo[s]+=1
            return
        
        for i in range(1,7):
            _back_tracking(n-1,s+i)
    
    _back_tracking(n,0)
    total=sum(memo.values())
    return [i/total for i in memo.values()]


def dicesProbability1(n: int) -> list:
    dp = [1 / 6] * 6
    for i in range(2, n + 1):
        tmp = [0] * (5 * i + 1)
        for j in range(len(dp)):
            for k in range(6):
                tmp[j + k] += dp[j] / 6
        dp = tmp
    return dp
