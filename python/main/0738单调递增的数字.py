
def monotoneIncreasingDigits(n: int) -> int:

    a = list(str(n))
    for i in range(len(a)-1,0,-1):
        if int(a[i]) < int(a[i-1]):
            a[i-1] = str(int(a[i-1]) - 1)
            a[i:] = '9' * (len(a) - i)  
    return int("".join(a)) 



print(ord('1')-1)