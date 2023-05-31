
def maxSumDivThree(nums: list) -> int:
    # 余数为i的最大和
    dp=[0]*3

    for n in nums:

        # 把n加入到dp只有三种情况
        a=dp[0]+n
        b=dp[1]+n
        c=dp[2]+n

        # 因为都是正整数，所以肯定越加越大
        # 但是余数不同的最大和之间大小还要确定
        dp[a%3]=max(dp[a%3],a)
        dp[b%3]=max(dp[a%3],b)
        dp[c%3]=max(dp[a%3],c)
    return dp[0]