class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        ans=0
        for i in stones:
            if i in jewels:
                ans+=1
        return ans
        
