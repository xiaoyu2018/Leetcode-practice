
# nxn矩阵
def spiralOrder(matrix: list) -> list:
    res=[]
    n=len(matrix)
    
    for i in range(0,n>>1):
        
        for j in range(i,n-i-1):
            res.append(matrix[i][j])
        for j in range(i,n-i-1):
            res.append(matrix[j][n-i-1])
        for j in range(n-i-1,i,-1):
            res.append(matrix[n-i-1][j])
        for j in range(n-i-1,i,-1):
            res.append(matrix[j][i])

    if(n%2==1):
        res.append(matrix[n//2][n//2])
    return res

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
'''
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16 
'''