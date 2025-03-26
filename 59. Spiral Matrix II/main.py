class Solution:
    def generateMatrix(self, n):
        # Initialize an empty n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Initialize variables for traversal
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1  # Start from 1
        
        while top <= bottom and left <= right:
            # Move right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            
            # Move down
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # Move left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1
            
            # Move up
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        
        return matrix
