import sys
from collections import deque

# ----------no.1-------------
N=int(input())

dependencies=[[int(i)-1 for i in input().strip().split(" ")][1:] for _ in range(N)]
in_degrees=[0]*N

# 计算每个节点的入度
for d in dependencies:
    for i in d:
        in_degrees[i]+=1

# 将入度为零的点加入栈
q=deque([i for i in range(N) if in_degrees[i]==0])

# 拓扑排序
res=0
cnt=len(q)

while(len(q)):
    
    size=len(q)
    res+=1
    for _ in range(size):
        crt=q.popleft()
        for i in dependencies[crt]:
            in_degrees[i]-=1
            if(in_degrees[i]==0):
                cnt+=1
                q.append(i)
        
print(res if cnt==N else -1)

# ----------no.2-------------
