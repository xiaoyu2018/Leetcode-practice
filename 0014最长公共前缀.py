

strs = ["ads","a"]

# 暴力
def longestCommonPrefix1( strs: list) -> str:
    
    for i in range(200):
        try:
            ch=strs[0][i]
            for j in strs:
                if(ch!=j[i]):
                    return j[:i] 
        except:
            return strs[0][:i]
            
# 分治
def longestCommonPrefix2( strs: list) -> str:
    
    def _lcp(start,end):
        if(start==end):
            return strs[start]
        mid=(start+end)//2
        
        llcp=_lcp(start,mid)
        rlcp=_lcp(mid+1,end)

        min_len=min(len(llcp),len(rlcp))
        for i in range(min_len):
            if(llcp[i]!=rlcp[i]):
                return llcp[:i]
        return llcp[:min_len]

    return "" if(not strs) else _lcp(0,len(strs)-1)




    

print(longestCommonPrefix2(strs))