class Solution(object):
    def reverseWords(self, s):
        l = s.split(" ")
        h = ''
        for i in l:
            h+=i[::-1] + ' '
        return h[:-1]