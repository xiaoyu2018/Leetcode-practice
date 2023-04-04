
def findNumberIn2DArray(matrix: list, target: int) -> bool:

    def _binary_search(line:list):
        nonlocal target
        l=0
        r=len(line)-1
        
        while(l<=r):
            mid=(l+r)>>1
            if(line[mid]==target):
                return line[mid]
            elif(line[mid]>target):
                r=mid-1
            else:
                l=mid+1
        return None
    
    for line in matrix:
        res=_binary_search(line)

        if(res):
            return True
    
    return False

import bisect
def findNumberIn2DArray1(matrix: list, target: int) -> bool:
    
    for row in matrix:
        idx=bisect.bisect_left(row,target)
        if(idx<len(row) and row[idx]==target):
            return True
    return False

def findNumberIn2DArray2(matrix: list, target: int) -> bool:
    if(not len(matrix) or not len(matrix[0])):
        return False
    m,n=len(matrix),len(matrix[0])
    
    i=0
    j=n-1
    while(0<=i<m and 0<=j<n):
        if(target==matrix[i][j]):
            return True
        elif(target<matrix[i][j]):
            j-=1
        else:
            i+=1
    return False

print(findNumberIn2DArray2([[1,1]],2))