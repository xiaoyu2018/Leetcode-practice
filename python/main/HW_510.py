# 1
def _one():
    # nums=[10,20,50,80,1,1]
    nums=[1]*1000
    st=[]

    
    def _solve(item:int):
        if(len(st)==0):
            st.append(item)
            return
        if(item==st[-1]):
            st.pop()
            _solve(item*2)
            return
        if(len(st)>=3):
            s=0
            count=0
            for i in range(len(st)-1,-1,-1):
                count+=1
                s+=st[i]
                if(s==item):
                    for i in range(count):
                        st.pop()
                    _solve(item*2)
                    return
                if(s>item):
                    break
        
        st.append(item)
    
    for n in nums:
        _solve(n)

    for v in st[::-1]:
        print(v,end=" ")

# 2
def _two():
    def _is_pwd(num:int):
        s=str(num)
        for i in range(1,len(s)):
            if(s[i]!=s[0]):
                return False
        return True

    m=input()
    n=int(input())
    k=input()

    op={
        "+":lambda a,b:a+b,
        "-":lambda a,b:a-b,
        "*":lambda a,b:a*b,
    }
    size=len(m)
    res=-1
    
    for i in range(size):
        for j in range(i+1,size+1):
            tmp=int(m[i:j])
            pwd=op[k](tmp,n)
            if(_is_pwd(pwd)):
                res=max(res,tmp)
    print(res)

# 3
def _three():
    m=int(input())
    n=int(input())
    graph=[[0]*m for _ in range(m)]

    for _ in range(n):
        x,y,v=(int(i) for i in input().strip().split(" "))
        graph[x-1][y-1]=v
    start=int(input())-1
    time_comsumed=-graph[start][start]
    memo=set()
    services=set()
    res_time=0

    def _dfs(start:int):
        nonlocal res_time,time_comsumed

        time_comsumed+=graph[start][start]
        res_time=max(res_time,time_comsumed)
        memo.add(start)
        for i in range(m):
            if(i in memo):
                continue
            if(graph[start][i]!=0):
                time_comsumed+=graph[start][i]
                res_time=max(res_time,time_comsumed)
                services.add(i)
                _dfs(start=i)
                time_comsumed-=graph[start][i]
        time_comsumed-=graph[start][start]
        memo.remove(start)

    _dfs(start)
    print(len(services)+1)
    print(res_time)

if __name__=='__main__':
    _three()