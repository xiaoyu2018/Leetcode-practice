a = "11"
b = "1"

def addBinary(a: str, b: str) -> str:
    return str(bin(int(a,base=2)+int(b,base=2)))[2:]



print(addBinary(a,b))