
def getRow(rowIndex: int) -> list:

    if(rowIndex<2):
        return [1]*(rowIndex+1)
    
    prev=[1,1]
    for i in range(2,rowIndex+1):
        crt=[1]
        
        for j in range(1,i+1):
            crt.append(1 if(j==i) else prev[j-1]+prev[j]) 
        prev=crt    

    return crt

print(getRow(0))