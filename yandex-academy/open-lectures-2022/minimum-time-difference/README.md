# Minimum time difference

## Description:

Every day `n` commuter trains arrive at the station. According to the given train schedule, determine the minimum time between the arrival of two different trains.

## Note:

Input: In the first line, enter the number of trains `n` (`1 ≤ n ≤ 2 × 10^4`). In the second line, enter `n` 24-hour clock time points in HH:MM format (`0 ≤ HH ≤ 23, 0 ≤ MM ≤ 59`) separated by whitespace.

Output: Print one number - the minimum minutes difference between the arrival of two trains.

## Examples:

```
Input: 2
       23:59 00:00
Output: 1
```
```
Input: 3
       00:00 23:59 00:00
Output: 0
```
