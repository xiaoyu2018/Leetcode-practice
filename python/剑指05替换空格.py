

def replaceSpace1(s: str) -> str:
    return s.replace(" ","%20")


def replaceSpace2(s:str)->str:
    res=""

    for i in s.split(" "):
        res+=i+"%20"
    
    return res[:-3]


    