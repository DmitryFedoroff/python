# Count of positive numbers in a segment

## Description:

Given a sequence of numbers and queries of a certain type, determine how many positive numbers are there in the segment from index `L` to `R`.

## Note:

Input: The first line contains the number `n` (`1 ≤ n ≤ 100,000`) — the length of the sequence.

In the second line, a sequence of `n` integers is entered, all numbers in absolute value do not exceed `100,000`. The numbering in the sequence starts from one.

The third line contains the number `q` (`1 ≤ q ≤ 100,000`) — the number of queries.

Each of the following `q` lines contains queries — two indices `l` and `r` (`1 ≤ l ≤ r ≤ n`).

Output: For each query, output the count of positive numbers in the segment.

## Examples:

```
Input: 5
       2 -1 2 -2 3
       4
       1 1
       1 3
       2 4
       1 5
Output: 1
        2
        1
        3
```

