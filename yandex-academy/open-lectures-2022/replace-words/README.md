# Replace words

## Description:

In order to save tone powder in the printer cartridge, it was decided to shorten some words in the text. To do this, a dictionary of words to which longer words can be shortened was compiled. A word from the text can be shortened if a word that is the beginning of a word from the text is found in the dictionary. For example, if the word `cat` is in the list, then the words from the text `catalogue`, `category` and other words beginning with `cat` can be shortened to `cat`.

If a word from the text can be shortened to several words from the dictionary, it should be shortened to the shortest word.

## Note:

Input: In the first line, enter words from the dictionary. The words consist of small Latin letters and separated by whitespace. It is guaranteed that the dictionary is not empty and the number of words in the dictionary does not exceed 1000 characters, and the length of the words is 100 characters. In the second line, enter words of the text (they also consist only of small Latin letters), separated by whitespace. The number of words in the text does not exceed `10^5` and the total number of letters in them does not exceed `10^6`.

Output: Print the text in which the replacements were made.

## Examples:

```
Input: a b
       abdafb basrt casds dsasa a
Output: a b casds dsasa a
```
```
Input: aa bc aaa
       a aa aaa bcd abcd
Output: a aa aa bc abcd
```
