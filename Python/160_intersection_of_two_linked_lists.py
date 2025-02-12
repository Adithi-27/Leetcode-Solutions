# -*- coding: utf-8 -*-
"""160. Intersection of Two Linked Lists.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13b2CB46rUfLyBasmK7CplQX16e9EVyjI
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1