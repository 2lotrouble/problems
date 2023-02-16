class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans = []
        d = max(candies)
        for i in candies:
            if i+extraCandies >= d:
                ans.append(True)
            else:
                ans.append(False)
        return ans