
# 回溯
def wordBreak1(s: str, wordDict: list) -> bool:
    size=len(s)
    memo=[-1]*size
    
    def _back_tracking(start:int=0):
        nonlocal s,size
        if(start==size):
            return True

        for i in range(start,size):
            if(s[start:i+1] in wordDict and _back_tracking(i+1)):
                return True

        return False
    
    return _back_tracking()


# 完全背包
# 单词是物品，字符串是背包
def wordBreak2(s: str, wordDict: list) -> bool:
    n=len(s)+1
    dp=[False]*n
    dp[0]=True

    for j in range(1,n):
        for word in wordDict:
            dp[j]=dp[j] or (dp[j-len(word)] and s[j-len(word):j]==word)
        print(dp)
    return dp[-1]

print(wordBreak2("catsanddog", ["cats", "dog", "and", "cat"] ))
    
