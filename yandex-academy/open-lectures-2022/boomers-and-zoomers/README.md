# Boomers and Zoomers

## Description:

The dog walking area is a place where people of different ages gather and socialize. At one of the grounds in Eastern Biryulevo, dog owners are very friendly and invite each other to a birthday party.

Person `x` does not invite a person `y` to a birthday party if at least one of the conditions is met:

- (Age of person `y`) <= `0.5` * (Age of person `x`) + `7`

- (Age of person `y`) > (Age of person `x`)

- (Age of person `y`) > `100` and at the same time (Age of person `x`) < `100`

In all other cases, person `x` invites person `y` to a birthday party.

Determine the total number of birthday invitations.

## Note:

Input: In the first line, enter number `n` (`1 ≤ n ≤ 100000`). In the second line, enter numbers - age of people separated by whitespace. The age ranges between `1` and `120`.

Output: Print the total number of birthday invitations.

## Examples:

```
Input: 2
       16 16
Output: 2
```
```
Input: 3
       17 16 18
Output: 2
```
```
Input: 5
       120 25 30 100 105
Output: 4
```
