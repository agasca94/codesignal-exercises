def countClouds(skyMap):
    count = 0
    for row in range(len(skyMap)):
        for col in range(len(skyMap[row])):
            if skyMap[row][col] == '1':
                count += 1
                discover_cloud(skyMap, row, col)

    return count


def discover_cloud(m, row, col):
    if row < 0 or row == len(m):
        return
    if col < 0 or col == len(m[row]):
        return
    if m[row][col] != '1':
        return

    # Clear the current cloud position to avoid cycles
    m[row][col] = '0'

    up = (row + 1, col)
    right = (row, col + 1)
    down = (row - 1, col)
    left = (row, col - 1)

    for nxt in [up, right, down, left]:
        discover_cloud(m, *nxt)



# Non-recursive solution (using an array as a stack)
def countClouds(skyMap):
    clouds = 0
    stack = []
    for i in range(len(skyMap)):
        for j in range(len(skyMap[i])):
            if skyMap[i][j] == '1':
                clouds += 1
                
                pos = (i, j)
                while pos:
                    x, y = pos
                    skyMap[x][y] = '0'
                    
                    if x > 0 and skyMap[x - 1][y] == '1':
                        stack.append((x, y))
                        pos = (x - 1, y)
                    elif y > 0 and skyMap[x][y - 1] == '1':
                        stack.append((x, y))
                        pos = (x, y - 1)
                    elif x < len(skyMap) - 1 and skyMap[x + 1][y] == '1':
                        stack.append((x, y))
                        pos = (x + 1, y)
                    elif y < len(skyMap[x]) - 1 and skyMap[x][y + 1] == '1':
                        stack.append((x, y))
                        pos = (x, y + 1)
                    elif stack:
                        pos = stack.pop()
                    else:
                        pos = None
                        
    return clouds
                        
                        