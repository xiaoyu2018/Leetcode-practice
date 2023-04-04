

def isAnagram1(s: str, t: str) -> bool:
    memo=dict()

    for i in s:
        if(i not in memo.keys()):
            memo[i]=1
        else:
            memo[i]+=1
        
    for i in t:
        if(i not in memo.keys()):
            return False
        
        memo[i]-=1
        if(memo[i]<0):
            return False

    return False if sum(memo.values()) else True


def isAnagram2(s: str, t: str) -> bool:
    memo=[0]*26

    for i in s:
        memo[ord(i)-97]+=1
    

    for i in t:
        idx=ord(i)-97
        memo[idx]-=1

        if(memo[idx]<0):
            return False

    return False if(sum(memo)) else True

print(isAnagram2("ab","a"))
        