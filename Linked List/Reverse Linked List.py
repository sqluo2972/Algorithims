# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:08:20 2020

LeetCode
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Recursive:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        return self.helper(head)
        
    def helper(self,head,prev=None):
        if not head:return prev
        Next , head.next = head.next , prev
        return self.helper(Next,head)
        
class Iterative:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
            
        return prev
    
"""
step1 : 1 -> null
step2 : 2 -> 1 -> null
step3 : 3 -> 2 -> 1 -> null
.....


"""