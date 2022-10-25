# Buy and sell

## Description:

You have `$1000` that you plan to invest effectively. You are given the prices for `1000` cubic meters of gas for `n` days. You can buy gas once with all the money on day `i` and sell it on one of the following days `j`, `i < j`. Determine the numbers of days for buying and selling gas to maximize profits.

## Note:

Input: In the first line, enter the number of days `n` (`1 ≤ n ≤ 100000`). In the second line, enter `n` numbers - prices for `1000` cubic meters of gas on each of the days. The price is an integer from `1` to `5000`. Days are numbered from `1`.

Output: Print two numbers `i` and `j` - the numbers of the days for buying and selling gas. If it is impossible to make a profit, print two zeros.

## Examples:

```
Input: 6
       10 3 5 3 11 9
Output: 2 5
```
```
Input: 4
       5 5 5 5
Output: 0 0
```
