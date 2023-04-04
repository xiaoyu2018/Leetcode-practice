ransomNote="a"
magzine="b"

# map
def canConstruct(ransomNote: str, magazine: str) -> bool:
    memo=dict()
    for i in magazine:
        if(i not in memo.keys()):
            memo[i]=1
        else:
            memo[i]+=1
    
    for i in ransomNote:
        if(i not in memo.keys()):
            return False
        
        memo[i]-=1

        if(memo[i]<0):
            return False
    
    return True

# 数组更快
def canConstruct(ransomNote: str, magazine: str) -> bool:
    memo=[0]*26

    for i in magazine:
        idx=ord(i)-ord('a')
        memo[idx]+=1
    
    for i in ransomNote:
        idx=ord(i)-ord('a')
        memo[idx]-=1
        if(memo[idx]<0):
            return False

    return True