import random

def generate_maze(width, height):
    maze = [[0 for _ in range(width)] for _ in range(height)]

    def carve_path(x, y):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)  

        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy

            if 1 <= nx < height - 1 and 1 <= ny < width - 1 and maze[nx][ny] == 0:
                maze[nx][ny] = 1 
                maze[x + dx][y + dy] = 1 

                carve_path(nx, ny)

    maze[1][1] = 1
    carve_path(1, 1)

    #Hardcode paths around the goal due to errors in the maze generation
    goal_x, goal_y = height - 2, width - 2

    maze[goal_x][goal_y - 1] = 1 

    maze[goal_x - 1][goal_y] = 1

    return maze
