class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        step1 = cost[0]
        step2 = cost[1]

        if len(cost)<=2:
            return min(step1, step2)

        for i in range(2, len(cost)):
            least = min(step1, step2)
            current = cost[i] + least
            step1 = step2
            step2 = current

        return min(step1, step2)