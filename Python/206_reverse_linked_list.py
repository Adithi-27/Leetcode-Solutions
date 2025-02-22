# -*- coding: utf-8 -*-
"""206. Reverse Linked List.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13b2CB46rUfLyBasmK7CplQX16e9EVyjI
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''if not head or not head.next:
            return head

        reversed_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return reversed_head'''

        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev