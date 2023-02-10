class Solution(object):
    def moveZeroes(self, nums):
        s = 0
        for i in nums:
            if i == 0:
                s += 1
        for i in range(s):
            nums.remove(0)
        print(nums)

        for i in range(s):
            nums.append(0)

        print(s, nums)
