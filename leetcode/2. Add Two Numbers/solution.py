# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        x = str(l1)
        y = str(l2)
        a = []
        b = []
        for i in x:
            if i.isdigit():
                a.append(i)
        for i in y:
            if i.isdigit():
                b.append(i)
        a.reverse()
        b.reverse()
        dig1=''
        dig2=''
        for i in a:
            dig1+=i
        for i in b:
            dig2+=i
        dig1=int(dig1)
        dig2=int(dig2)
        summ=dig1+dig2
        summ=str(summ)
        ans=''
        for i in summ[::-1]:
            ans+=i
            ans+=","
        return ListNode(ans[:-1])
