class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        rowsBefore = self.generate(numRows - 1)
        current = [1] * numRows
        
        for i in range(1, numRows - 1):
            current[i] = rowsBefore[-1][i - 1] + rowsBefore[-1][i]
        
        rowsBefore.append(current)
        return rowsBefore