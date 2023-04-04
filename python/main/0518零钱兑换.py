
def change(amount: int, coins: list) -> int:
    dp=[0]*(amount+1)
    dp[0]=1

    for c in coins:
        for j in range(c,amount+1):
            dp[j]+=dp[j-c]
    

    return dp[-1]

print(change(5, [1, 2, 5]))