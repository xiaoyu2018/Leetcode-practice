

def removeDuplicates( s: str) -> str:
    st=[]
    
    for c in s:
        if(not st or st[-1]!=c):
            st.append(c)
            continue
        st.pop()
    return "".join(st)


print(removeDuplicates("aba"))