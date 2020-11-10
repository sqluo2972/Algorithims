# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:48:35 2020

@author: c0096

LeetCode
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""
import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        left = 0
        right = len(nums) - 1
        mid = (left+right) // 2
        
        while nums[mid] != target:
            
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            mid = (left+right) // 2
            
        for i in range(mid,right+1):
            if nums[i] != target:
                right = i-1
                break
                
        for i in range(mid,left-1,-1):
            if nums[i] != target:
                left = i+1
                break
                
        return [left,right]