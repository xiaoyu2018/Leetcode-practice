# 9x9
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]




def solveSudoku(board: list) -> None:
    
    keys=[(i,j) for i in range(9) for j in range(9) if board[i][j]=='.']
    total=len(keys)
    valid=False
    
    row_memo=[[False]*10 for _ in range(9)]
    col_memo=[[False]*10 for _ in range(9)]
    block_memo=[[[False]*10 for _a in range(3)] for _b in range(3)]
    
    for i in range(9):
        for j in range(9):
            if(board[i][j]!='.'):
                n=int(board[i][j])
                row_memo[i][n]=True
                col_memo[j][n]=True
                block_memo[i//3][j//3][n]=True

    def _check(x,y,num):
        if(row_memo[x][num]):
            return True
        if(col_memo[y][num]):
            return True
        if(block_memo[x//3][y//3][num]):
            return True
        return False
    
    def _solve(count=0):
        nonlocal total,valid

        if(count==total):
            valid=True
            return

        for i in range(1,10):
            if(valid):
                return
            
            x,y=keys[count]
            
            if(_check(x,y,i)):
                continue
            
            row_memo[x][i]=True
            col_memo[y][i]=True
            block_memo[x//3][y//3][i]==True
            board[x][y]=str(i)

            _solve(count+1)
            row_memo[x][i]=False
            col_memo[y][i]=False
            block_memo[x//3][y//3][i]==False
            
    _solve()
    return board
   

# solveSudoku(board)
# for line in board:
#     print(line)

