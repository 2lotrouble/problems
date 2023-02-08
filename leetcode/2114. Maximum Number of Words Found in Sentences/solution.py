class Solution(object):
    def mostWordsFound(self, sentences):
        ans = 0
        for i in sentences:
            if len(i.split(" "))>ans:
                ans=len(i.split(" "))
        return ans
            