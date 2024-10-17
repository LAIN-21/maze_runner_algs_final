from collections import deque

def bfs(start, goal, maze):
    queue = deque([start])  
    visited = set([start]) 
    parent = {start: None}  

    while queue:
        current = queue.popleft()

        if current == goal:
            return reconstruct_path(parent, goal)

        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited and maze[neighbor[0]][neighbor[1]] == 1:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    return None

def reconstruct_path(parent, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]
    return path[::-1]

def get_neighbors(pos, maze):
    neighbors = []
    x, y = pos
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]): 
            neighbors.append((nx, ny))
    return neighbors
