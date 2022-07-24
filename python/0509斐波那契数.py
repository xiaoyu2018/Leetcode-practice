

def fib1(n: int) -> int:
    if(n==0 or n==1):
        return n
    
    return fib1(n-1)+fib1(n-2)

memo=dict()

# 记忆化
def fib2(n:int)->int:

    if(n==1 or n==0):
        return n
    
    
    f_n_1=memo[n-1] if n-1 in memo.keys() else fib2(n-1)
    f_n_2=memo[n-2] if n-2 in memo.keys() else fib2(n-2)

    memo[n-1]=f_n_1    
    memo[n-2]=f_n_2

    return f_n_2+f_n_1    
    
# 改写迭代
def fib3(n:int)->int:
    tmp=[0,1]
    if(n==0 or n==1):
        return n
    
    res=0

    while(n>1):
        n-=1
        res=tmp[0]+tmp[1]
        tmp[0]=tmp[1]
        tmp[1]=res


    return res

print(fib3(4))