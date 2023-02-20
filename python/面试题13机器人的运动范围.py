
def movingCount(m: int, n: int, k: int) -> int:

    def _bit_sum(num: int):
        return sum([int(n) for n in str(num)])

    
    matrix=[[0]*n for _ in range(m)]
    
    for i in range(m):
        if(_bit_sum(i)>k):
            break
        matrix[i][0]=1
    for i in range(n):
        if(_bit_sum(i)>k):
            break
        matrix[0][i]=1
            
    temp=-1
    res=0
    while(res!=temp):
        temp=res
        for i in range(1,m):
            for j in range(1,n):
                if(matrix[i][j-1] or matrix[i-1][j]):
                    matrix[i][j]=(_bit_sum(i)+_bit_sum(j))<=k

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if(matrix[i][j+1] or matrix[i+1][j]):
                    matrix[i][j]=(_bit_sum(i)+_bit_sum(j))<=k
        res=sum([sum(i) for i in matrix])

    return res

print(movingCount(100,100,20))