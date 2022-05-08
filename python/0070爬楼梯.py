# 找出规律 1 2 3 5 8 13，缺第一项的斐波那契数列
# 在n-1阶爬1和n-2阶爬2可以得到全部的爬到n阶的情况
# 递归
def climbStairs1(n):
    if(n==1):
        return 1
    if(n==2):
        return 2
    
    return climbStairs1(n-1)+climbStairs1(n-2)

# 迭代
def climbStairs2(n):
    if(n==1):
        return 1
    if(n==2):
        return 2
    x1,x2=1,2
    res=0
    
    while(n-2>0):
        res=x1+x2
        x1=x2
        x2=res
        n-=1
    
    return res

print(climbStairs2(5))