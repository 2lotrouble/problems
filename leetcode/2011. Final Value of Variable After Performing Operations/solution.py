class Solution(object):
    def finalValueAfterOperations(self, operations):
        d = {"++X":1,"X++":1,"--X":-1,"X--":-1}
        ans = 0
        for i in operations: 
            ans+=d[i]
        return ans 