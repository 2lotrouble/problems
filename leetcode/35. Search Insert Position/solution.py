class Solution(object):
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0
        if target == nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        nums.append(1)
        i = 0
        while (nums[i] < target):
            i += 1

        return i