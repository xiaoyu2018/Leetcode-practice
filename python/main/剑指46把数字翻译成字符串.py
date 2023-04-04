
def translateNum(num: int) -> int:
    nums=[int(i) for i in str(num)]
    dp=[1]*(len(nums)+1) #最前面补一个位置

    for i,v in enumerate(nums[1:],1):
        if(nums[i-1]!=0 and -1<v+nums[i-1]*10<26):
            dp[i+1]=dp[i]+dp[i-1]
        else:
            dp[i+1]=dp[i]
        

    return dp[-1]

print(translateNum(12258))