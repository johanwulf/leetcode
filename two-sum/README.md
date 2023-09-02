## Problem

https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

## Solution

The greedy solution for this problem would be to loop through the array and comparing each element against each element and return the indices if they add up to the specified sum. This would give us a time complexity of O(n).

A better way to solve this problem is to use a set and loop through the array once. When we get a value, we see if the difference between the number we get from the loop and the total sum is in the set. If it is, we simply return the positions of those values.
