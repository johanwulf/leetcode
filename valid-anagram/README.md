## Problem

https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**
**Input:** s = "anagram", t = "nagaram"
**Output:** true

**Example 2:**
**Input:** s = "rat", t = "car"
**Output:** false

**Constraints:**
1 <= s.length, t.length <= 5 \* 10<sup>5</sup>
s and t consist of lowercase English letters.

## Solution

### Sorting the incoming strings

If we sort the two incoming strings and then compare them, we will know if they are an anagram or not.

**Pseudo code**

```
1. Sort strings
2. Compare strings on equality, and return result
```

**Time complexity**  
If we sort and compare the strings, we will have a time complexity of O(n log n) as that is the time complexity of the sorting algorithm.

### Using dictionaries

Instead of sorting the two strings, giving us the time complexity of O(n log n), we can use dictionaries to keep track of the frequency of the letters.

**Pseudo code**

```
1. Check if length of the strings are the same, if not, return false
2. Create two empty dictionaries
3. For each letter in the strings, add 1 to the count
4. Compare the two dictionaries and return the result
```

**Time complexity**
The time complexity will be O(n) as we loop through the length of the strings.
