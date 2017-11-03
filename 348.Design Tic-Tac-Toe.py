class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.size = n
        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.diagonal = 0
        self.antidiagonal = 0
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player not in range(3):
            return 0
        offset = (-1,1)[player == 1]
        self.rows[row] += offset
        self.cols[col] += offset
        if row == col:  self.diagonal += offset 
        if row+col == self.size-1:  self.antidiagonal += offset 
        
        isLine = (abs(self.rows[row]) == self.size or
                  abs(self.cols[col]) == self.size or
                  abs(self.diagonal) == self.size or
                  abs(self.antidiagonal) == self.size)
        
        return player if isLine else 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
