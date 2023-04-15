import sys

# 1 按要求构造01串
# 2 二维dp找回文子串
# size:第一行输入 nums：第二行输入
def solve4(size:int,nums:list):
    chars=[] #直接将元素放入数组，避免重复构造字符串的性能消耗
    flag=1 #记录当前重复元素是1还是0

    # 构造01串
    for i in range(size):
        chars.extend([flag]*nums[i])
        flag=int(not flag)
    

    # 二维dp求回文子串，dp中(i,j)对元素意义为：下标i-j之间的子串是否为回文串
    # dp方式：双指针i,j遍历整个chars数组
    #        如果chars[i]不等于chars[j]：dp[i][j]为0不变
    #        如果chars[i]等于chars[j]：i==j或i+1=j时，dp[i][j]=1
    #                                 j>i+1时，dp[i][j]=dp[i+1][j-1]
    l=len(chars)
    dp=[[0]*l for _ in range(l)]

    # i<=j，只需遍历上三角矩阵，从右下向左上遍历
    for i in range(l-1,-1,-1):
        for j in range(i,l):
            if(chars[i]==chars[j]):
                if(j-i<2):
                    dp[i][j]=1
                    continue
                else:
                    dp[i][j]=dp[i+1][j-1]
    # print(dp)
    # 将dp数组中所有元素相加即可
    return sum([sum(i) for i in dp])

# 回溯
def solve3(nlr:list,zos:str,edge:list):
    n,l,r=nlr
    bits=[int(i) for i in zos]
    
    # 建立邻接表
    table=[[0]*n for _ in range(n)]
    for i,j in edge:
        table[i][j]=1
    
    res=0

    # 找到根节点
    def _dfs(tmp="0b"):
        nonlocal l,r

        

    return res

def solve2(n:int):
    
    global res
    tmp=0

    # 只需找到n/2处
    for i in range(1,n>>1):
        global res
        # 找最小公倍数,n-i>=i大
        j=n-i
        while(j%(n-i) or j%i):
            j+=1
        if(j>tmp):
            tmp=j
            res=(i,n-i)
    
    return res

# 一维dp
def solve4_2(size:int,nums:list):
    chars=[] #直接将元素放入数组，避免重复构造字符串的性能消耗
    flag=1 #记录当前重复元素是1还是0

    # 构造01串
    for i in range(size):
        chars.extend([flag]*nums[i])
        flag=int(not flag)
    

    # 二维dp求回文子串，dp中(i,j)对元素意义为：下标i-j之间的子串是否为回文串
    # dp方式：双指针i,j遍历整个chars数组
    #        如果chars[i]不等于chars[j]：dp[i][j]为0不变
    #        如果chars[i]等于chars[j]：i==j或i+1=j时，dp[i][j]=1
    #                                 j>i+1时，dp[i][j]=dp[i+1][j-1]
    l=len(chars)
    dp=[0]*l
    res=0

    # i<=j，只需遍历上三角矩阵，从右下向左上遍历
    for i in range(l-1,-1,-1):
        for j in range(l-1,i-1,-1):
            if(chars[i]==chars[j]):
                if(j-i<2):
                    dp[j]=1
                    continue
                else:
                    dp[j]=dp[j-1]
            else:
                dp[j]=0

        res+=sum(dp)

    return res


if __name__ =='__main__':
    # from time import time
    # a=time()
    # print(solve4(60,[99]*60))
    # print(time()-a)
    # print("----------------------------------------")
    # a=time()
    # print(solve5(60,[99]*60))
    # print(time()-a)
    print(solve2(6))

    