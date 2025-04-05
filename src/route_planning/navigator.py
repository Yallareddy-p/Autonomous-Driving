import numpy as np
from scipy.spatial import Voronoi
from scipy.spatial.distance import euclidean

class Navigator:
    def __init__(self):
        self.grid_size = 10  # Size of the grid for path planning
        self.safety_margin = 50  # Safety margin around obstacles
        
    def plan_route(self, objects, lanes, pedestrians):
        # Create a grid representation of the environment
        grid = self._create_grid(objects, lanes, pedestrians)
        
        # Find the optimal path using A* algorithm
        start = (0, 0)  # Starting point (can be modified)
        goal = (grid.shape[0]-1, grid.shape[1]-1)  # Goal point (can be modified)
        
        path = self._a_star(grid, start, goal)
        
        return path
    
    def _create_grid(self, objects, lanes, pedestrians):
        # Create a grid with obstacles
        grid = np.ones((100, 100))  # Example grid size
        
        # Mark obstacles from object detections
        for obj in objects:
            x1, y1, x2, y2, _, _ = obj
            grid[y1:y2, x1:x2] = 0
            
        # Mark obstacles from pedestrian detections
        for ped in pedestrians:
            x1, y1, x2, y2, _ = ped
            grid[y1:y2, x1:x2] = 0
            
        # Mark lane boundaries as obstacles
        for lane in lanes:
            for point in lane:
                x, y = point
                grid[y-self.safety_margin:y+self.safety_margin,
                     x-self.safety_margin:x+self.safety_margin] = 0
                    
        return grid
    
    def _a_star(self, grid, start, goal):
        # A* path planning algorithm
        def heuristic(a, b):
            return euclidean(a, b)
            
        def get_neighbors(node):
            neighbors = []
            for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_node = (node[0] + i, node[1] + j)
                if (0 <= new_node[0] < grid.shape[0] and
                    0 <= new_node[1] < grid.shape[1] and
                    grid[new_node] == 1):
                    neighbors.append(new_node)
            return neighbors
            
        open_set = {start}
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start, goal)}
        
        while open_set:
            current = min(open_set, key=lambda x: f_score.get(x, float('inf')))
            
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]
                
            open_set.remove(current)
            
            for neighbor in get_neighbors(current):
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    if neighbor not in open_set:
                        open_set.add(neighbor)
                        
        return None  # No path found 