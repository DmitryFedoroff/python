# Applications selection

## Description:

A lecture room is given, where several professors want to give their lectures. For scheduling, the professors have submitted applications of the form [`si`, `fi`] - the start and end times of the lecture. The lecture is considered an open half-interval, that is, some lecture can start at the moment when another one finishes, without a break. Make a class schedule so as to fulfill the maximum number of applications.

## Note:

In the first line, enter a natural number `n` (`1 ≤ n ≤ 1000`) - the total number of applications. Then `n` lines with descriptions of applications are entered - two numbers in each `si` and `fi`. It is guaranteed that `si` < `fi`. The time of the beginning and the end of the lecture is a natural number, not exceeding `1440` (in minutes from the beginning of the day).

Output: Print one number - the maximum number of applications that can be fulfilled.

## Examples:

```
Input: 1
       5 10
Output: 1
```
```
Input: 3
       1 5
       2 3
       3 4
Output: 2
```
