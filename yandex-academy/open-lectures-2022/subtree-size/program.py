import sys

sys.setrecursionlimit(100000)

def dfs(now, neighbours, subtree_size):
    subtree_size[now] = 1
    for next in neighbours[now]:
        if subtree_size[next] == -1:
            subtree_size[now] += dfs(next, neighbours, subtree_size)
    return subtree_size[now]

def store_subtrees_size(n):
    neighbours = []
    for i in range(n + 1):
        neighbours.append([])

    for i in range(n - 1):
        a, b = map(int, input('Enter vertices connected by edge: ').split())
        neighbours[a].append(b)
        neighbours[b].append(a)
       
    subtree_size = [-1] * (n + 1)
    dfs(1, neighbours, subtree_size)
    return subtree_size[1:]

n = int(input('Number of vertices: '))
