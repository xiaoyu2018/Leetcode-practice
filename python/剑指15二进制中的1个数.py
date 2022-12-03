
def hammingWeight(n: int) -> int:
    
    origin_num=n
    s=0

    while(n>0):
        n>>=1
        
        s+=n
    
    return origin_num-s

print(hammingWeight(9))