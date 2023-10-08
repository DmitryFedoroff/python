def dfs(vertex, graph, subtree_size):
    subtree_size[vertex] = 1
    for neighbor in graph[vertex]:
        if subtree_size[neighbor] == -1:
            subtree_size[vertex] += dfs(neighbor, graph, subtree_size)
    return subtree_size[vertex]


def compute_subtrees_size(num_vertices):
    graph = [[] for _ in range(num_vertices + 1)]
    for _ in range(num_vertices - 1):
        a, b = map(int, input('Enter vertices connected by edge: ').split())
        graph[a].append(b)
        graph[b].append(a)

    subtree_size = [-1] * (num_vertices + 1)
    dfs(1, graph, subtree_size)
    return subtree_size[1:]


if __name__ == '__main__':
    num_vertices = int(input('Number of vertices: '))
    print('Size of subtree for each of vertices: ', *compute_subtrees_size(num_vertices))
