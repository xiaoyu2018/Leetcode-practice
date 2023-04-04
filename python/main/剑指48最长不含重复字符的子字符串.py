
def lengthOfLongestSubstring(s: str) -> int:
    size=len(s)

    if(size<1):
        return 0
    
    dp=[1]*size

    for i in range(1,size):
        j=i-1
        while(j>-1 and s[j]!=s[i]): j-=1

        dp[i]=dp[i-1]+1 if i-j>dp[i-1] else i-j
    
    return max(dp)

lengthOfLongestSubstring("dvdf")