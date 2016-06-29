class Solution(object):
    def duplicate(self, num):
        dic={}
        for j in xrange(9):
            if num[j]!='.':
                if num[j] not in dic:
                    dic[num[j]]=1
                else:
                    return False
        return True
            
    def isValidSudoku(self, board):
        for i in xrange(9):
            board[i]=list(board[i])
            
        for i in xrange(9):
            if not self.duplicate(board[i]):
                return False
            if not self.duplicate([row[i] for row in board]):
                return False
                
        for k in xrange(3):
            for l in xrange(3):
                temp=[]
                for i in xrange(3*k,3*(k+1)):
                    for j in xrange(3*l,3*(l+1)):
                        temp+=[board[i][j]]
                if not self.duplicate(temp):
                    return False
        
        return True
