
# 暴力
def countSubstrings(s: str) -> int:
    
    def _is_tenet(l,r):
        nonlocal s
        for i in range(r-l+1):
            if(s[l+i]!=s[r-i]):
                return False
        return True

    res=0
    size=len(s)
    for i in range(size):
        for j in range(i,size):
            res+=_is_tenet(i,j)

    return res


# dp
def countSubstrings1(s: str) -> int:
    
    size=len(s)
    res=0
    dp=[[False]*size for _ in range(size)]

    # i<=j，只需遍历上三角矩阵。
    for i in range(size-1,-1,-1):
        for j in range(i,size):
            if(s[i]==s[j]):
                if(j-i<2):
                    dp[i][j]=True
                    res+=1
                    continue

                elif(dp[i+1][j-1]):
                    dp[i][j]=True
                    res+=1
    return res

print(countSubstrings1("aaa"))