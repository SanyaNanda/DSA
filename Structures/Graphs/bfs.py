# graph represented a sadjaceny list in form of dictionary
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

# List for visited nodes.
visited = [] 
#Initialize a queue
queue = []    

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
  print ("\n") 

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    

