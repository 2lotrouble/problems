class Solution(object):
    def longestCommonPrefix(self, strs):
        s=[]
        for i in strs:
            s.append(str(i))

        l = len(s[0])

        for i in s:
            if l>len(i):
                l=len(i)

        ans = ""
        cou = 0
        for i in range(l):
            for j in range(len(s)-1):
                if s[j][:i]==s[j+1][:i]:
                    cou+=1
                    
            if cou == len(s)-1:
                ans=s[0][:i+1]
            else:
                break
            cou=0
        return ans
            
