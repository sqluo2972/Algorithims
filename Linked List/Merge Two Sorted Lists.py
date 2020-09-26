# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:00:10 2020

@author: c0096

LeetCode
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4



"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        current = head
        
        while l1 or l2:
            
            if not l1:
                current.next = ListNode(l2.val)
                l2 = l2.next
            elif not l2:
                current.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val <= l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:                        # if l2.val > l1.val                  
                current.next = ListNode(l2.val)         
                l2 = l2.next
                
            current = current.next
            
        return head.next


class LeetCodeSolution:
    def mergeTwoLists1(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
            
        