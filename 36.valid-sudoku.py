#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        judgeList = []
        for i in board:
            for j in i:
                if(j != '.'):
                    if(j in judgeList):
                        return False
                    judgeList.append(j)
            judgeList = []
        
        for i in range(9):
            for j in range(9):
                if(board[j][i] != '.'):
                    if(board[j][i] in judgeList):
                        return False
                    judgeList.append(board[j][i])
            judgeList = []
        
        judgeList = [[], [], []]
        for i in range(9):
            for j in range(3):
                if(board[i][j] != '.'):
                    if(board[i][j] in judgeList[0]):
                        return False
                    judgeList[0].append(board[i][j])
            for j in range(3, 6):
                if(board[i][j] != '.'):
                    if(board[i][j] in judgeList[1]):
                        return False
                    judgeList[1].append(board[i][j])
            for j in range(6, 9):
                if(board[i][j] != '.'):
                    if(board[i][j] in judgeList[2]):
                        return False
                    judgeList[2].append(board[i][j])
            
            print(judgeList)
            if(i%3 == 2):
                judgeList = [[], [], []]
        
        return True
"""
[[".",".",".",".","5",".",".","1","."]
,[".","4",".","3",".",".",".",".","."]
,[".",".",".",".",".","3",".",".","1"]
,["8",".",".",".",".",".",".","2","."]
,[".",".","2",".","7",".",".",".","."]
,[".","1","5",".",".",".",".",".","."]
,[".",".",".",".",".","2",".",".","."]
,[".","2",".","9",".",".",".",".","."]
,[".",".","4",".",".",".",".",".","."]]
"""
# @lc code=end

