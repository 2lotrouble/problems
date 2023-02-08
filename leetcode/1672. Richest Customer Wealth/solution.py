class Solution(object):
    def maximumWealth(self, accounts):
        ans=0
        x=0
        for i in accounts:
            for j in i:
                x+=j
            if x>ans:
                ans=x
            x=0
        return ans
