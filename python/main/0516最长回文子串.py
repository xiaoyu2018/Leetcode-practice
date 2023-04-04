# dp
def longestPalindromeSubseq(s: str) -> int:
    size=len(s)
    
    dp=[
        [1 if i==j else 0 for i in range(size)] 
        for j in range(size)
    ]

    for i in range(size-1,-1,-1):
        for j in range(i+1,size):
            if(s[i]==s[j]):
                dp[i][j]=dp[i+1][j-1]+2
                
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        
    return dp[0][size-1]