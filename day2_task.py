import heapq

# ---------------- PART 1: A* SEARCH ----------------
graph = {
    'S': {'A': 3, 'C': 2},
    'A': {'B': 4},
    'B': {'D': 5},
    'C': {'D': 2},
    'D': {}
}
h = {'S': 4, 'A': 7, 'B': 5, 'C': 2, 'D': 0}

def a_star(start, goal):
    open_list = [(h[start], 0, start, [start])]   # (f, g, node, path)
    explored = []
    while open_list:
        f, g, node, path = heapq.heappop(open_list)
        if node in explored:
            continue
        explored.append(node)
        print(f"Exploring {node}:  g = {g}, h = {h[node]}, f = {f}")
        if node == goal:
            return path, g, explored
        for nxt, cost in graph[node].items():
            g2 = g + cost
            f2 = g2 + h[nxt]
            heapq.heappush(open_list, (f2, g2, nxt, path + [nxt]))
    return None, None, explored

print("=== PART 1: A* Search ===")
path, cost, explored = a_star('S', 'D')
print("\nNodes explored :", " -> ".join(explored))
print("Final path     :", " -> ".join(path))
print("Total cost     :", cost)

# ---------------- PART 2: HILL CLIMBING ----------------
def f(x):
    return (x - 5) ** 2 + 10

def hill_climbing(x, step=0.5):
    while True:
        print(f"x = {x:.2f}, f(x) = {f(x):.2f}")
        neighbors = [x - step, x + step]
        best = min(neighbors, key=f)
        if f(best) < f(x):
            x = best            # move to better neighbor
        else:
            return x            # no better neighbor -> stop

print("\n=== PART 2: Hill Climbing ===")
best_x = hill_climbing(x=0)
print(f"\nMinimum at x = {best_x:.2f}, f(x) = {f(best_x):.2f}")
