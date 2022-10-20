# Repeating number

## Description:

You are given a sequence of measurements of some quantity. It is required to determine whether any number was repeated, and the distance between repetitions did not exceed `k`.

## Note:

Input: In the first line, enter two numbers `n` and `k` (`1 ≤ n, k ≤ 10^5`). In the second line, enter `n` numbers. The numbers should be separated by whitespace and do not exceed `10^9` by their absolute values (modulus).

Output: Print `Yes` if there is a repeating number and the distance between repetitions does not exceed `k`, otherwise print `No`.

## Examples:

```
Input: 4 2
       1 2 3 1
Output: No
```
```
Input: 4 1
       1 0 1 1
Output: Yes
```
```
Input: 6 2
       1 2 3 1 2 3
Output: No
```
