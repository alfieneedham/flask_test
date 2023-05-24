from functions.naive_priority_queue import NaivePriorityQueue
from math import inf

def dijkstras_algorithm(graph, start, destination):

    def find_index(vertex):
        for i in range(len(vertices)):
            if vertices[i][0] == vertex:
                return(i)
            
    queue = NaivePriorityQueue()
    vertices = []
    for vertex in graph:
        # tuple: (vertex name, vertex children, parent, distance to vertex)
        vertices.append([vertex, graph[vertex], None, inf])

    vertices[find_index(start)][2] = start
    vertices[find_index(start)][3] = 0
    queue.enqueue(start, 0)
    
    # while queue.is_empty() == False:
    #     currentVertex = queue.dequeue()
    #     for neighbour in currentVertex[0].neighbours:
    #         if vertices[find_index(currentVertex[0])][2] + neighbour[1] < vertices[find_index(neighbour[0])][2]:
    #             vertices[find_index(neighbour[0])][2] = vertices[find_index(currentVertex[0])][2] + neighbour[1]
    #             vertices[find_index(neighbour[0])][1] = currentVertex[0]
    #             queue.enqueue(neighbour[0], vertices[find_index(currentVertex[0])][2] + neighbour[1])  
                   
    # currentVertex = vertices[find_index(destination)]
    # distance = currentVertex[2]
    # while currentVertex[0] != start:
    #     try:
    #         path.append(currentVertex[0])
    #         currentVertex = vertices[find_index(currentVertex[1])]
    #     except:
    #         print("No valid path.")
    #         quit()
            
    # path.append(start)
    # reversedPath = reversed(path)
    # return(reversedPath, distance)