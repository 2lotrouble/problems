class Solution(object):
    def shuffle(self, nums, n):
        x=[]
        y=[]
        ans=[]
        for i in range(len(nums)):
            if i<n:
                x.append(nums[i])
            else:
                y.append(nums[i])
        for i in range(n):
            ans.append(x[i])
            ans.append(y[i])
        return ans