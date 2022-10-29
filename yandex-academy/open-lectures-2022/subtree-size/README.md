# Size of subtree

## Description:

Given an undirected tree suspended by vertex `1`. For each vertex calculate how many vertices are contained in the subtree suspended from this vertex.

## Note:

Input: In the first line, enter `V` number of vertices (`3 ≤ V ≤ 100000`). In the next `V-1` lines, enter pairs of numbers - the vertices connected by an edge.

Output: Print `V` numbers - size of subtree for each of the vertices.

## Examples:

```
Input: 4
       1 2
       1 3
       1 4
Output: 4 1 1 1
```
```
Input: 7
       1 2
       1 3
       1 4
       5 1
       5 6
       5 7
Output: 7 1 1 1 3 1 1
```

