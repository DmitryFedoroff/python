# Socks

## Description:

There is a table of length `L`. There are `N` socks on the table such that no sock exceeds the borders of the table. Then there is a clever girl who wants to measure the thickness of the socks covering the table at `M` points.

## Note:

Input: In the first line, enter the length of table `L` (`1 ≤ L ≤ 10000`), the total number of socks `N` (`1 ≤ N ≤ 10000`) and the total number of points `M` (`1 ≤ M ≤ 100000`). Each number `L`, `N` and `M` is separated by whitespace. Then go the input file which gives `N` pairs of numbers `L ≤ R` from `1` to `L` - the left and right ends of the socks. Then enter `M` numbers from `1` to `L` - the points of girl's interest. All numbers are integers.

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

