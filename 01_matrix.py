"""
Time: O(m*n)
Space: O(m*n)
Leet: Accept
Problems: None. Referred to solution explained in session.
"""

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        #initialize a result matrix with 0s
        result = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        #call dfs on each element and update
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                result[row][col] = self.dfs(matrix, result, row, col)
        return result

    def dfs(self, matrix, result, row, col):
        if row < 0 or col < 0 or row > len(matrix)-1 or col > len(matrix[0])-1: #edge
            return float('inf')

        if matrix[row][col] == 0: #base
            return 0

        #check for surrounding 1s
        if row>0 and matrix[row-1][col]==0:
            return 1
        if col>0 and matrix[row][col-1]==0:
            return 1
        if row<len(matrix)-1 and matrix[row+1][col] == 0:
            return 1
        if col<len(matrix[0])-1 and matrix[row][col+1] == 0:
            return 1


        #utilize dp
        up = left = float('inf')
        #if result has already been obtained for up and left, update those values
        if row > 0 and result[row-1][col]!=0:
            up = result[row-1][col]
        if col > 0 and result[row][col-1]!=0:
            left = result[row][col-1]

        #find values for down and right with dfs
        down = self.dfs(matrix, result, row+1, col)
        right = self.dfs(matrix, result, row, col+1)

        return 1+ min(up,down,left,right)
