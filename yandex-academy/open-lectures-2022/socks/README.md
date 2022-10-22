# Socks

## Description:

There is a table of length `l`. There are `n` socks on the table such that no sock exceeds the borders of the table. Then there is a clever girl, who wants to measure the thickness of the socks covering the table at `m` points.

## Note:

Input: The input file gives first `l` (`1 ≤ L ≤ 10000`), `n` (`1 ≤ N ≤ 10000`), `m` (`1 ≤ M ≤ 100000`). Then go `n` pairs of numbers `l ≤ r` from `1` to `l` - the left and right ends of the socks. Then `m` numbers from `1` to `l` are the points of girls's interest. All numbers are integers.

Output: Print one number - the thickness of the sock coating at each point.

## Examples:

```
Input: 22 18 8
       6  11
       10 15
       3  18
       1  19
       10 17
       1  10
       6  16
       20 21
       1  1
       12 21
       5  9
       1  10
       5  10
       6  11
       5  6
       7  11
       1  19
       13 15
       5
       22
       19
       3
       8
       16
       16
       21
Output: 8
        0
        3
        5
        11
        6
        6
        2
```

