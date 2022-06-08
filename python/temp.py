# from functools import lru_cache

# @lru_cache(None)
# def fibo1(n:int):
#     if(n in [1,2]):
#         return 1

#     return fibo1(n-1)+fibo1(n-2)


# memo=dict()
# def fibo2(n:int):
#     if(n in [1,2]):
#         memo[n]=1

#     if(n in memo.keys()):
#         return memo[n]
    
#     val=fibo2(n-1)+fibo2(n-2)
#     memo[n]=val

#     return val

# # print(fibo2(999))

# def createArray2D(h,w):
#     return [[0]*w for j in range(h)]
#     # return [[0]*w]*h 错误写法，低维数组地址相同

# a=createArray2D(3,4)
# a[0][0]=1
# print(a)


nums=[1,2,1,1,1,1]
s=11

def SpiralMatrix(n:int):

    mat=[[0]*n for i in range(n)]
    
    crt_elem=1
    loop_time=0
    while(crt_elem<=n*n):

        if(crt_elem==n*n):
            mat[n//2][n//2]=crt_elem
            break
        for i in range(loop_time,n-loop_time-1):
            mat[loop_time][i]=crt_elem
            crt_elem+=1
        for i in range(loop_time,n-loop_time-1):
            mat[i][n-1-loop_time]=crt_elem
            crt_elem+=1
        for i in range(n-loop_time-1,loop_time,-1):
            mat[n-1-loop_time][i]=crt_elem
            crt_elem+=1
        for i in range(n-loop_time-1,loop_time,-1):
            mat[i][loop_time]=crt_elem
            crt_elem+=1
        
        loop_time+=1
    
    return mat
    
for line in SpiralMatrix(5):
    print(line)