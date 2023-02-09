class Solution(object):
    def sortedSquares(self, nums):
        b = []
        for i in nums:
            b.append(pow(i, 2))

        return sorted(b)
