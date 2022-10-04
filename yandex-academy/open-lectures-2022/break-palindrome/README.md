# Break palindrome

## Description:

A palindrome is a word, phrase, or sentence reads the same backward or forward.

Given a palindromic string of lowercase English letters. Replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

A string `A` is lexicographically smaller than a string `B` (of the same length) if in the first position where `A` and `B` differ, `A` has a character strictly smaller than the corresponding character in `B`. For example, `abcc` is lexicographically smaller than `abcd` because the first position they differ is at the fourth character, and `c` is smaller than `d`.

## Note:

Input: Palindrome string that consists of only lowercase English letters. The length of the string does not exceed 1000 letters.

Output: Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

## Examples:

```
Input: abba
Output: aaba
```
```
Input: a
Output:
```

## Explanation:

There are a few ways to make `abba` not a palindrome, such as `zbba` and `abaa`. Of all the ways, `aaba` is the lexicographically smallest.

There is no way to replace a single character to make `a` not a palindrome, so return an empty string.

