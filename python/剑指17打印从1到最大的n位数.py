
def printNumbers(n: int) -> list:
    if(n==0):
        return []
    max_num="9"*n
    return [i for i in range(1,int(max_num)+1)]

print(printNumbers(0))

