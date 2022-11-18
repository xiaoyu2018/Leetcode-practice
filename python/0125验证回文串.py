
def isPalindrome(s: str) -> bool:
    valid_chars=[str(i) for i in range(10)]+[chr(i) for i in range(ord("a"),ord("z")+1)]
    left=0
    right=len(s)-1

    while(left<right):
        l_c=s[left].lower()
        if(l_c not in valid_chars):
            left+=1
            continue

        r_c=s[right].lower()
        if(r_c not in valid_chars):
            right-=1
            continue

        if(l_c!=r_c):
            return False
        left+=1
        right-=1
    
    return True


# print(isPalindrome("A man, a plan, a canal: Panama"))

print("a".isalnum())