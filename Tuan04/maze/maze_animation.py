import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import heapq
import time
# ===================== MOVEMENT CONSTANT =====================
actions = [(1,0), (-1,0), (0,1), (0,-1)]

# ===================== MIN HEAP =====================
class MinHeap:
    def __init__(self):
        self.items = []
    def empty(self):
        return len(self.items) == 0
    def push(self, item):
        heapq.heappush(self.items, item)
    def pop(self):
        return heapq.heappop(self.items)

# ===================== UTILS =====================
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclid_distance(a, b):
    return np.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
# ===================== DRAW MAZE =====================
def draw_grid(ax, maze):
    m = len(maze)
    n = len(maze[0])
    for i in range(m + 1):
        ax.plot([0, n], [i, i], linewidth = 0.3,  color='black')
    for j in range(n + 1):
        ax.plot([j, j], [0, m], linewidth = 0.3, color='black')

    for i in range(0, m):
        for j in range(0, n):
            if maze[i][j] == 1:
                ax.fill([j, j+1, j+1, j],
                [i, i, i+1, i+1],
                color='black')


    ax.set_xlim(0, n)
    ax.set_ylim(0, m)
    ax.invert_yaxis()
    ax.axis("off")

def reconstruct_path(parent, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return path  

# ===================== A* =====================
def AStar(maze, start, goal):
    m, n = maze.shape
    g = {start: 0}
    parent = {start: None}
    closed = set()


    heap = MinHeap()
    heap.push((0, start))

    visited = []


    while not heap.empty():
        _, cur = heap.pop()
        if cur in closed:
            continue
        visited.append(cur)
        closed.add(cur)
        # Vẽ node đang duyệt
        x, y = cur
        print(x,y)

        if cur == goal:
            break

        for dx, dy in actions:
            nx, ny = cur[0] + dx, cur[1] + dy
            if 0 <= nx < m and 0 <= ny < n:
                if maze[nx][ny] == 1:
                    continue
                nxt = (nx, ny)
                new_cost = g[cur] + 1
                if nxt not in g or new_cost < g[nxt]:
                    g[nxt] = new_cost
                    f = new_cost + euclid_distance(nxt, goal)
                    heap.push((f, nxt))
                    parent[nxt] = cur

    return visited, reconstruct_path(parent, goal)

def update(i):
    if i < len(visited):
        x, y = visited[i]
        ax.fill([y, y+1, y+1, y],
                [x, x, x+1, x+1],
                color='lightblue')
    else:
        j = i - len(visited)
        x, y = path[j]
        ax.fill([y, y+1, y+1, y],
                [x, x, x+1, x+1],
                color='yellow')

        
# ===================== MAIN =====================
if __name__ == "__main__":
    m, n = 30, 30
    maze = np.random.choice([0, 0], size=(m, n), p=[0.8, 0.2])
    start = (0, 0)
    goal = (m-1, n-1)
    maze[start] = 0
    maze[goal] = 0
    fig, ax = plt.subplots(figsize=(10, 10))
    draw_grid(ax, maze)
    # Vẽ start & goal
    ax.fill([0,1,1,0],[0,0,1,1], color="green")
    ax.fill([n-1,n,n,n-1],[m-1,m-1,m,m], color="red")

    visited, path = AStar(maze, start, goal)

    frames = visited + path

    ani = FuncAnimation(fig, update, frames=len(frames), interval=40, repeat =False)

    ani.save("astar_maze.gif", writer=PillowWriter(fps=10))
    plt.show()
    plt.close()
