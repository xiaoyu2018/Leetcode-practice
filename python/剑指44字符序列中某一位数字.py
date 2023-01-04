
# 模拟
def findNthDigit(n: int) -> int:

    crt_num=0
    crt_idx=0
    i=0

    while(i<n):
        
        size=len(str(crt_num))

        while(True):
            if(crt_idx==size-1 or i==n):
                break
            crt_idx+=1
            i+=1
            
        if(i==n):
            break
        crt_num+=1
        i+=1
        crt_idx=0
    
    return int(str(crt_num)[crt_idx])
        

# 按规律计算
def findNthDigit1(n: int) -> int:
        d, count = 1, 9
        while n > d * count:
            n -= d * count
            d += 1
            count *= 10
        index = n - 1
        start = 10 ** (d - 1)
        num = start + index // d
        digitIndex = index % d
        return num // 10 ** (d - digitIndex - 1) % 10


print(findNthDigit1(0))