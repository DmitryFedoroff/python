import sys

sys.setrecursionlimit(100000)

def dfs(now, neighbours, subtree_size):
    subtree_size[now] = 1
    for next in neighbours[now]:
        if subtree_size[next] == -1:
            subtree_size[now] += dfs(next, neighbours, subtree_size)
    return subtree_size[now]

n = int(input('Number of vertices: '))
