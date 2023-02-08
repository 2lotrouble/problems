class Solution(object):
    def minPartitions(self, n):
        d = 0
        for i in n:
            if int(i)>d:
                d=int(i)
        return d