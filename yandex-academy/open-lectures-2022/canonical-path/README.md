# Canonical path

## Description:

For a given string, which is an absolute address in UNIX operating systems, you need to get a canonical path.

In UNIX operating systems, `.` corresponds to the current directory and `..` corresponds to the parent directory, while we assume that any number of consecutive points greater than two corresponds to the directory with this name (consisting of dots). `/` is a separator of nested directories, and several consecutive `/` should be interpreted as one `/`.

The canonical path should have the following properties:

- Always start with one `/`

- Any two nested directories are separated by exactly one `/` sign

- The path does not end with `/` (except for the root directory, which consists only of the `/` character)

- There are only directories in the canonical path, i.e. there is not a single occurrence of `.` or `..` as a match to the current or parent directory

## Note:

The string is entered with an absolute address and its length should not exceed 100.

## Examples:

```
Input: /home/
Output: /home
```
```
Input: /../
Output: /
```
```
Input: /home//foo/
Output: /home/foo
```

## Explanation:

In the first example, you need to remove the `/` at the end of the string.

In the second example, it is impossible to climb above the root directory.

In the third example, several consecutive `/` should be replaced by one, and it is also necessary to remove `/` at the end of the string.
