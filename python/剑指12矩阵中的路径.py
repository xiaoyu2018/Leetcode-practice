
def exist(board: list, word: str) -> bool:
    m=len(board)
    n=len(board[0])
    l=len(word)
    directoins=[(0,-1),(-1,0),(0,1),(1,0)]
    visited=set()

    def _dfs(i,j,k):
        nonlocal m,n,l

        if(board[i][j]!=word[k]):
            return False
        if(k==l-1):
            return True
        
        visited.add((i,j))
        for x,y in directoins:
            new_i,new_j=i+x,j+y
            if(0<=new_i<m and 0<=new_j<n and (new_i,new_j) not in visited):
                if(_dfs(new_i,new_j,k+1)):
                    return True
        visited.remove((i,j))

        return False


    for i in range(m):
        for j in range(n):
            if(_dfs(i,j,0)):
                return True
    return False