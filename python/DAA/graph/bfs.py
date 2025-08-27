graph = {  0:[1,2]   ,1:[2] , 2:[3,4] ,3:[3], 4:[0] }

def bfs(root_node):
    que=[root_node]
    viseted= [root_node]
    while que:
        node=que.pop(0)
        for neighbour in graph[node]:
            if neighbour not in viseted:
                viseted.append(neighbour)
                que.append(neighbour)
    print(viseted)

bfs(1)