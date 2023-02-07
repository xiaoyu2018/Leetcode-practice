from itertools import permutations

# built-in
def permutation1(s: str) -> list:
    return set(["".join(i) for i in permutations(s)])

def permutation2(s: str) -> list:
    res=set()
    temp=[]
    bool_memo=[False]*len(s)

    def _back_tracking():
        
        if(len(temp)==len(s)):
            res.add("".join(temp))
            return
        
        for i,v in enumerate(s):
            if(not bool_memo[i]):
                temp.append(v)
                bool_memo[i]=~bool_memo[i]
                _back_tracking()
                temp.pop()
                bool_memo[i]=~bool_memo[i]

    _back_tracking()
    return list(res)

