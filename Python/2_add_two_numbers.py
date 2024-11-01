# -*- coding: utf-8 -*-
"""2. Add Two Numbers.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mtFGWQakSj51MCqet43h6xs0_rk4slsw
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to help build the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Loop until both lists are exhausted and there is no carry left
        while l1 or l2 or carry:
            # Get the values from the current nodes; if a list is exhausted, use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry for the next digit
            current.next = ListNode(total % 10)  # Set the current digit as the next node

            # Move pointers to the next elements in the lists and result
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the result list, which is next of dummy node
        return dummy_head.next