# 暴力
def IsPalindrome1(x:int):
    if(x<0):
        return False
    array=[]
    while(x>0):
        val=x%10
        array.append(val)
        x//=10

    
    size=len(array)
    for i in range(size//2):
        if(array[size-i-1]!=array[i]):
            return False
    
    return True


# 转化为字符串
def IsPalindrome2(x:int):

    return str(x)==str(x)[::-1]

print(IsPalindrome2(-121))