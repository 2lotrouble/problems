class Solution(object):
    def romanToInt(self, s):
        d={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "O":0}
        s+="O"
        ans=d[s[0]]
        for i in range(1,len(s)-1):
            if d[s[i]]<d[s[i+1]]:
                ans+=d[s[i+1]]-d[s[i]]
            elif d[s[i]]<=d[s[i-1]]:
                ans+=d[s[i]]
            elif (i==1) and (d[s[i]]>d[s[i-1]]):
                ans=d[s[i]]-ans
        return ans