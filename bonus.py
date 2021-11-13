row = len(matrix)
col = len(matrix[0])

visited = [[False for i in range(col)]for j in range(row)]

# start = (5, 6)
x = start[0]
y = start[1]


Dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
bfs = {}
bfs_length = {}
path = []
# Mark the source cell as visited
visited[x][y] = True
     
# Create a queue for BFS
q = deque()
     
q.append(start) #  Enqueue source cell
     
# Do a BFS starting from source cell
while q:
    store_dist = {}
    curr = q.popleft() # Dequeue the front cell
    path.append(curr)
    # If we have reached the destination cell,
    # we are done
    if curr[0] == end[0] and curr[1] == end[1]:
        break
    print(curr)
    # Otherwise enqueue its adjacent cells
    for i in range(4):
        a = curr[0] + Dir[i][0]
        b = curr[1] + Dir[i][1]    
        
    # if adjacent cell is valid, has path 
    # and not visited yet, enqueue it.
        if (a >= 0 and b >= 0 and a < row and b < col and matrix[a][b] != 'x' and (a, b) and not visited[a][b]):
            dist = math.sqrt((a-end[0])**2 + (b-end[1])**2)
            store_dist[(a, b)] = weights[a][b] + dist
            bfs[(a, b)] = curr
            #select point based on distance array
        if i == 3:
            if store_dist == {}:
                #if it doesn't quit traverse path to find a new way :v
                for point in reversed(bfs.values()):
                    for i in range(4):
                        a = point[0] + Dir[i][0]
                        b = point[1] + Dir[i][1]
                        if (a >= 0 and b >= 0 and a < row and b < col and matrix[a][b] != 'x' and (a, b) and not visited[a][b]):
                            dist = math.sqrt((a-end[0])**2 + (b-end[1])**2)
                            store_dist[(a, b)] = weights[a][b] + dist
            
            store_dist = dict(sorted(store_dist.items(), key=lambda item: item[1]))
            print(store_dist)
            if len(store_dist.values()) > 1 and len(set(store_dist.values())) == 1:
                for key, val in store_dist.items():
                    bfs_length[key] = len(bfs_search(matrix,key,end))
                bfs_length = dict(sorted(bfs_length.items(), key=lambda item: item[1]))
                for k,length in bfs_length.items():
                    visited[k[0]][k[1]] = True
                    q.append(k)
                    break
            else:
                for key, val in store_dist.items():
                    visited[key[0]][key[1]] = True
                    q.append(key)
                    break
    print()
p = {}
cell = end
while cell != start:
    p[bfs[cell]] = cell 
    cell = bfs[cell]
final = list(p.values())
final.append(start)
finalPath = final[::-1]
visualize_maze(matrix,bonus_points,start,end, list(bfs.values()))
visualize_maze(matrix,bonus_points,start,end, finalPath)