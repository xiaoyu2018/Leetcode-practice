from math import log2,log,e

def isPowerOfTwo1( n: int) -> bool:
    try:
        return True if int(log2(n))==log2(n) else False
    except:
        return False

# 二分
def isPowerOfTwo2(n: int) -> bool:
    if(n<=0):
        return False
    if(n in [1,2,4,8,16,32,64,128]):
        return True
    left=0
    right=n>>5

    while(left<=right):
        mid=(left+right)>>1
        temp=1<<mid
        if(temp==n):
            return True
        if(temp>n):
            right=mid-1
        else:
            left=mid+1
    return False


# 梯度下降(精度不够)
def isPowerOfTwo3(n:int):
    lr=1e-6
    x=32
    loss=pow(2,x)-n
    while(loss>1e-7):
        d=x*log(2,e)
        x-=lr*d
        loss=pow(2,x)-n
    return True if 0.99999<(x-int(x))<=1 else False

# 暴力
def isPowerOfTwo4(n:int):
    if(n<0):
        return False
    x=1
    while(x<pow(2,31)-1):
        if(x==n):
            return True
        x<<=1

    return False

# 打表
def isPowerOfTwo5(n:int):
    def _getData():
        x=1
        while(x<pow(2,31)-1):
            print(x,end=",")
            x<<=1
    data={1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,
          2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824}
    return n in data

print(isPowerOfTwo5(257))