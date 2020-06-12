import numpy as np
from DFS import dfs
from Astar import a_star

grid = np.array([["G","H","I","J"],
                 ["L","M","N","O"],
                 ["Q","R","S","T"],
                 ["V","W","X","Y"]])

print("DFS output:")
dfs(grid, "W", "H")

print("A* output:")
a_star(grid, "W", "H")

