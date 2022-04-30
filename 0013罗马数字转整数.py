
def romanToInt(s: str) -> int:
    r2i={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    res=0
    temp=0

    for i in s:
        convert_num=r2i[i]
        if(temp<convert_num):
            res-=2*temp
            
        res+=convert_num
        temp=convert_num
    return res

print(romanToInt("LVIII"))
