
# 模拟
def generateMatrix(n:int):
    if(n==1):
        return [[1]]

    res=[[0]*n for i in range(n)]
    count=0
    i=j=0
    # 上下左右四种前进模式
    mode=0
    while(count<n*n):
        count+=1
        res[i][j]=count
        if(mode==0):
            j+=1
            if(not(j==n-1 or res[i][j+1])):
                continue
        if(mode==1):
            i+=1
            if(not(i==n-1 or res[i+1][j])):
                continue
        if(mode==2):
            j-=1
            if(not(j==0 or res[i][j-1])):
                continue
        if(mode==3):
            i-=1
            if(not(i==0 or res[i-1][j])):
                continue
        
        mode=(mode+1)%4


    return res

print(generateMatrix(4))