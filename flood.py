"""
Time : O(m*n)
Space: O(1)
Leet: Accepted
Problems: None
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        maxRow = len(image)
        maxCol = len(image[0])

        color = image[sr][sc] #find color to be changed

        if color == newColor: #edge
            return image

        def dfs(row,col):
            if image[row][col] == color:
                image[row][col] = newColor #replace color with new color
                #call dfs on neighbors
                if row-1 >= 0:
                    dfs(row-1,col)
                if row+1 < maxRow:
                    dfs(row+1,col)
                if col-1 >= 0:
                    dfs(row,col-1)
                if col+1 < maxCol:
                    dfs(row,col+1)
        dfs(sr,sc)
        return image
