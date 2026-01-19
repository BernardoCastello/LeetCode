# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:

        aux = ListNode(0, head)
        pre = aux

        while head and head.next:

            prim = head
            sec = head.next

            pre.next = sec
            prim.next = sec.next
            sec.next = prim

            pre = prim
            head = prim.next
        
        return aux.next

