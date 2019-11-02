def execute():
    print("Executing problem-14")

    pathCount = 0
    gridSize = 20
    stack = []
    
    stack.append((0, 0)) 
    
    while len(stack) > 0:
        node = stack.pop()
        if node[0] < gridSize and node[1] < gridSize:
            pathCount += 1
        if node[0] < gridSize:
            x = node[0] + 1
            stack.append((x, node[1]))
        if node[1] < gridSize:
            y = node[1] + 1
            stack.append((node[0], y))

    if gridSize > 0:
        pathCount += 1
    print("Path count = ", pathCount)

execute()
