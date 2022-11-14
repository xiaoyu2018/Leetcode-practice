
def generate(numRows: int) -> list:
    
    res=[[1],[1,1]]
    if(numRows<2):
        return res[:numRows]

    numRows-=1
    for n in range(2,numRows+1):
        crt=[1 if i==0 or i==n else res[n-1][i-1]+res[n-1][i] for i in range(n+1)]
        res.append(crt)
    
    return res

print(generate(15))