class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return n
        trib=[0, 1, 1]
        for i in range(3, n+1):
            next = trib[0]+trib[1]+trib[2]
            trib[0]=trib[1]
            trib[1]=trib[2]
            trib[2]=next
        return trib[2]
        