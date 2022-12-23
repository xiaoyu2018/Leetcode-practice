
def minArray(numbers: list) -> int:
    res=numbers[0]

    for i in range(1,len(numbers)):
        if(numbers[i]<numbers[i-1]):
            res=numbers[i]
    
    return res