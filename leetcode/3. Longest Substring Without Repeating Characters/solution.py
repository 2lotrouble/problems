class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        m = 1
        s = list(s)
        s.append("^")
        for i in range(len(s) - 1):
            d = i
            w = s[d]
            while (s[d + 1] not in w) and s[d + 1] != "^":
                m += 1
                w += s[d + 1]
                d += 1
            if m > ans:
                ans = m
            m = 1
        return ans

