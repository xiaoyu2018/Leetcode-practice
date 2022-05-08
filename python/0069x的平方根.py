

# 二分
def mySqrt1(x):
    right=x
    left=0

    while(left<=right):
        mid=int((left+right)>>1)

        if(mid*mid==x):
            return mid
        elif(mid*mid<x):
            if((mid+1)*(mid+1)>x):
                return mid
            left=mid+1
        
        else:
            right=mid-1


# 牛顿迭代
def mySqrt2(x):
    if(x==0):
        return 0
    # 初值取为x
    x_prim,x_hat=x,x

    while(True):
        x_hat=(x_hat+x/x_hat)/2
        if(abs(x_hat-x_prim)<0.1):
            return int(x_hat)
        x_prim=x_hat
    
x=1364655888
print(mySqrt2(x))
        
        