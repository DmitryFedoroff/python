# Path to file

## Description:

In the Xunil OS, information about all files and directories is stored in a special file in the following format:

```
emoh
 vonavi
  a.doc
  b.doc 
 vortep
  .bashrc
 vorodis
  onrop
   1.avi
   2.avi 
rav
 bil
```

Only file names contain a dot. Find the path to the file by the given file name. If there are several such files, output the path to the file written above.

## Note:

Input: In the first line, enter the name of the file you are looking for. In the second line, enter the total number of files and directories. The rest of the lines contain information about files and directories in the format specified above (a directory or a file inside another directory is separated by one extra space at the beginning of the line). The number of lines in the file and the number of characters in each line does not exceed `100`.

Output: Print the path to the file in the format `/directory/directory/.../file` It is guaranteed that there is such a file and the answer string length does not exceed `255`.

## Examples:

```
Input: 1.avi
       12
       emoh
        vonavi
         a.doc
         b.doc 
        vortep
         .bashrc
        vorodis
         onrop
          1.avi
          2.avi 
       rav
        bil
Output: /emoh/vorodis/onrop/1.avi
```

