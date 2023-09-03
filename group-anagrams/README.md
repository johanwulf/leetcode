## Problem

https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

## Solution

To be able to group the words together based on their letters we need to create a key from each word, which is the same for two words containing the same letters.
One approach to do this would be to sort the strings and use that as the key. The problem with sorting the string is that the time complexity for sorting algorithms is in the best case O(n log n) which is high. We can do better.

Instead of sorting the array, we can, for each word, create an array with 26 slots. For each letter in the word, we increment the corresponding position in the array, for instance:

['a', 'b', 'c'] would give us an array looking like [1, 1, 1, 0 .. 0]
