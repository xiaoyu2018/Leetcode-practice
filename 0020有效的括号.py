s="[]"

# 栈
def isValid(s: str) -> bool:
    bracket_map={"}":"{","]":"[",")":"("}
    stack=[]
    
    for i in s:
        if(i not in bracket_map):
            stack.append(i)
            
        else:
            if(not stack):
                return False

            top=stack.pop()
            if(bracket_map[i]!=top):
                return False

    return not stack
    
print(isValid(s))