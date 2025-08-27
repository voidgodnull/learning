graph = {  0:[1,2]   ,1:[2] , 2:[3,4] ,3:[3], 4:[0] }

def dfs(root_node,visited=set()):
    visited.add(root_node)
    print(visited)
    for neighbour in graph[root_node]:
        if neighbour  not in visited:
         dfs(neighbour,visited)

dfs (2)