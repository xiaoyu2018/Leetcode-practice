digits = [9,9,9]

# 进位隐藏
def plusOne1(digits:list):   
    for i in range(len(digits)-1,-1,-1):
        if(digits[i]==9):
            digits[i]=0
        else:
            digits[i]+=1
            return digits

    return [1]+digits

# 递归
def plusOne2(digits:list):
    # 首位需要进位
    if(not digits):
        return [1]

    if(digits[-1]<9):
        digits[-1]+=1
        return digits

    # 最后一位是9
    # 进位，将最后一位改为0，对前面的子序列进行加一操作
    return plusOne2(digits[:-1])+[0]

# 类型转换
def plusOne3(digits:list):
    ans=0
    for i in digits:
        ans=ans*10+i
    
    return [int(i) for i in str(ans+1)]

print(plusOne2(digits))
