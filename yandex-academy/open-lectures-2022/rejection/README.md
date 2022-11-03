# Rejection

## Description:

The chemical plant has a reactor that produces chemical substances whose formula is written as a string of upper and lower case Latin letters. Also, the plant has a list of desirable substances (substances of the first grade), which would like to get. A substance is called a first-grade substance if its formula is exactly the same as the formula from the list of desirable substances.

In addition, the plant is also interested in substances of the second- and third-grades. A substance is called a second-grade substance if it can be made into a substance from the list of desirable substances by replacing some capital letters with lower case letters and vice versa. A substance is called a substance of the third-grade if it is possible both to replace the letters from uppercase letters to lowercase letters and vice versa, and to replace any vowel letters (aeiou) with other vowel letters, so that a substance from the list of desirable letters is obtained.

In view of the difficult economic situation, it was decided not to throw out substances of the second- and third-grade and to find for each of them a similar substance from the list of desirable ones, and if several substances from the list of desirable ones can be obtained by transformations from the second- or third-grade, then it should be transformed to the substance which is earlier in the list of desirable ones.

## Note:

Input: In the first line, enter `n` (`1 ≤ n ≤ 5000`) - the number of substances on the list of desirable substances. In the second line, enter `n` words separated by whitespace - the list of desirable substances. In the third line, enter the number `k` (`1 ≤ k ≤ 5000`) - the number of substances obtained in the reactor. In the fourth line, enter `k` words separated by whitespace - the list of substances obtained in the reactor. The length of all words does not exceed 7.

Output: For each substance, print:

If it is a first-grade substance - the name of that substance.

If it is not a substance of the first-grade, but is a substance of the second-grade - the first from the list of desirable substances to which this substance can be transformed.

If it is not a first- or second-grade substance, but is a third-grade substance - the first from the list of desirable substances to which this substance can be converted.

Otherwise, print a blank line.

All words in the output should be separated by whitespace.

## Examples:

```
Input: 4
       LiTe lite bare Bare
       10
       Bare BARE Bear bear lite Lite LiTe leti leet leto
Output: Bare bare   lite LiTe LiTe LiTe  LiTe
```
```
Input: 1
       DeLay
       1
       delOy
Output: DeLay
```
