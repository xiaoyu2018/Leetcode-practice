
# 模拟（回溯）
def cuttingRope1(n: int) -> int:
    res=1
    path=[]

    def _traceback(start:int):
        nonlocal res,n

        for i in range(start,n+1):
            path.append(i)
            _traceback(i+1)
            path.pop()

        size=len(path)
        if(size):
            crt=path[0]

            for i in range(size-1,0,-1):
                crt*=(path[i]-path[i-1])
            
            res=max(res,crt)
            print(path)
    _traceback(1)
    return res


# 数学
def cuttingRope2(n: int) -> int:
    
    res=1

    # 这么写均等分割的遍历过程会有缺失，比如想要把10分成3份的情况
    # for i in range(2,n):
    #     crt=max(n%i,1)
    #     crt*=((n//i)**i)

    #     res=max(res,crt)
    
    for i in range(2,n):
        # 能除尽
        crt=None
        if(not(n%i)):
            crt=(n//i)**i
        else:
            crt=(n//i)**(i-(n%i))*(n//i+1)**(n%i)

        res=max(res,crt)
    return res

print(cuttingRope1(5))