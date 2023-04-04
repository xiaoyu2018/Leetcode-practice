

def repeatedSubstringPattern(s: str) -> bool:
    size=len(s)

    sub_size=0

    while(sub_size<size-1):
        sub_size+=1
        if(size%sub_size):
            continue

        if(s==s[:sub_size]*(size//sub_size)):
            return True
        
    return False

print(repeatedSubstringPattern("aasaas"))