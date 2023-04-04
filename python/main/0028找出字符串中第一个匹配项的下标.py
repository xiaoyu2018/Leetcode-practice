
def strStr(haystack: str, needle: str) -> int:
    m,n=len(haystack),len(needle)
    
    nxt=[0]*n # 最长相等前后缀数
    j=0 # 前缀末尾下标的后一位，等待判断
    
    # 创建nxt数组（以每个索引为结尾的子串的最长最长相等前后缀数）
    for i in range(1,n):
        # 找到最长相等前后缀数，或者或者j=0也没找到
        # 这里就是用到KMP的匹配回溯思想，当出现字符不相等时，不会重新从头暴力匹配
        # j-1（包含）前的前缀=i-1（包含）后缀
        # 当needle[j]!=needle[i]时，从j-1最长相等前后缀数重新匹配
        while(j>0 and needle[j]!=needle[i]):
            j=nxt[j-1]

        # j=0退出上面的循环时，needle[j]==needle[i]不一定成立
        if(needle[j]==needle[i]):
            j+=1
        nxt[i]=j

    # 找出第一个匹配的下标
    p=q=0
    while(p<m):
        
        if(haystack[p]==needle[q]):
            q+=1
            p+=1
        else:
            if(q==0):
                p+=1
            else:
                q=nxt[q-1]
        if(q==n):
            return p-q 

    return -1

print(strStr("aabaabaaf","aabaaf"))
