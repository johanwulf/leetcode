## Problem

https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**  
Input: nums = [1,2,3,1]  
Output: true

**Example 2:**  
Input: nums = [1,2,3,4]  
Output: false

**Example 3:**  
Input: nums = [1,1,1,3,3,4,3,2,4,2]  
Output: true

**Constraints:**  
1 <= nums.length <= 10<sup>5</sup>  
-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>

## Solution

The easiest solution for this problem is to use a set. A set is a data structure that only contains unique values.

We loop through the array and for each number check if it is already in the set, if it is, return true, if not, we add it to the set.

If the loop finishes, we know that there is no duplicates in the array. Otherwise, it will return true.

**Pseudo code**

```
1. Create an empty set.
2. For each value in the array:
   - If the value is already in the set, return true.
   - Add the value to the set.
3. Return false if no duplicate values are found in the array (the loop finishes)
```

**Time complexity**  
The solution will have a time complexity of O(n) as the worst case is that there is no duplicates, and then we would have to loop through the entire array.
