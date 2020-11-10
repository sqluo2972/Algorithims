# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:01:36 2020

@author: c0096

LeetCode
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2


"""
import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        return max(count.keys(),key = count.get)