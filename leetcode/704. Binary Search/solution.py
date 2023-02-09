class Solution(object):
    def search(self, nums, target):
        try:
            ans = nums.index(target)
        except ValueError:
            ans = -1
        return ans
