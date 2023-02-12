# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        run = head
        l = 0
        while run:
            l+=1
            run = run.next
        l = l//2
        while l:
            head = head.next
            print(head)
            l-=1
        return head