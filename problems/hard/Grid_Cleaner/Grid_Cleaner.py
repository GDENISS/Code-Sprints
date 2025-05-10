def GridCleaner(grid, column, row, n, direction=0):
    # Create a deep copy of the grid to avoid modifying the input
    grid = [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    
    # Current position and direction
    x, y = column, row
    dir = direction
    
    # Direction vectors: north, east, south, west
    dx = [0, 1, 0, -1]  # x changes
    dy = [-1, 0, 1, 0]  # y changes
    
    for _ in range(n):
        # Check if current position is valid
        if not (0)<= x < width and 0 <= y < height:
            break
            
        current = grid[y][x]
        
        if current == 1: 
            dir = (dir + 1) % 4
            grid[y][x] = 0
        else: 
            dir = (dir - 1) % 4
            grid[y][x] = 1
            
        x += dx[dir]
        y += dy[dir]
    
    return grid