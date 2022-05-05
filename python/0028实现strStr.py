

# 暴力
def strStr(haystack:str,needle:str):
    
    if(not needle):
        return 0
    h_len=len(haystack)
    n_len=len(needle)
    if(h_len<n_len):
        return -1

    for i,s in enumerate(haystack):
        if(s==needle[0]):
            for j,k in enumerate(needle):
                if((i+j)>=h_len):
                    return -1
                if(haystack[i+j]!=k):
                    break
                if(j==n_len-1):
                    return i
    return -1
    

print(strStr("mississippi","issipi"))
