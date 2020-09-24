# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:59:39 2020

@author: c0096

LeetCode
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [0]
Output: 0

Example 4:

Input: nums = [-1]
Output: -1

Example 5:

Input: nums = [-2147483647]
Output: -2147483647

 

Constraints:

    1 <= nums.length <= 2 * 104
    -231 <= nums[i] <= 231 - 1



"""
import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
                
        return max(nums)
            
"""        
 this method is Kadane's algo (Dynamic Programming,DP)
 if previous continuous sum is positive then we can keep caculating next num 
 but if it is negitive then it is not helpful to count in 
 Example: List = [1,2,3,-7,5]
 step 1: List = [1,3,3,-7,5], index = 1 ,List[0] > 0 ,so List[index] += List[0] 
 step 2: List = [1,3,6,-7,5]
 step 3: List = [1,3,6,-1,5]
 step 4: List = [1,3,6,-1,5] index = 4, since List[3] < 0 then don't count it in 
 final: return max(List)
"""