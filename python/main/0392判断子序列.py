s="aaa"
t="aaaaaa"

# 暴力
def isSubsequence(s: str, t: str) -> bool:
    if(not len(s)):
        return True
    if(len(s)>len(t)):
        return False
    
    idx=t.find(s[0])
    
    if(idx==-1):
        return False
    else:
        return isSubsequence(s[1:],t[idx+1:])

# dp
# dp[i][j] 表示以下标i-1为结尾的字符串s，和以下标j-1为结尾的字符串t的最大相同子序列，方便初始化
def isSubsequence1(s: str, t: str) -> bool:

    # 按上述方式规定dp后只需初始化dp二维数组为全零
    m=len(s)+1
    n=len(t)+1
    dp=[[0]*n for _ in range(m)]
    
    for i in range(1,m):
        for j in range(1,n):
            if(s[i-1]==t[j-1]):
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=dp[i][j-1] #相当于删掉了在t中不同的字符
    
    return dp[-1][-1]==m-1

print(isSubsequence1(s,t))

