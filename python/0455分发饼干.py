
g=[1,2,3]
s=[1,1]

def findContentChildren(g: list, s: list) -> int:
    g=sorted(g,reverse=True)
    s=sorted(s,reverse=True)

    count=0
    i=0
    j=0
    while(i<len(g) and j<len(s)):
        if(g[i]<=s[j]):
            count+=1
            j+=1
        i+=1
    
    return count