# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:40:33 2020

@author: c0096

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
            
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode()
        current = start
        Sum = 0             
       
        while l1 or l2 :            #The length might be different
            Sum //=10               #keep the carry 
            
            if l1:
                Sum += l1.val
                l1 = l1.next
            if l2:
                Sum += l2.val
                l2 = l2.next
                
            current.next = ListNode(Sum%10)
            current = current.next
                
        if Sum // 10 == 1:         # if has carry then carry in 
            current.next = ListNode(1)
        return start.next 
            