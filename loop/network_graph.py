from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, node1, node2):
        self.adjacency_list.setdefault(node1, [])
        self.adjacency_list.setdefault(node2, [])
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def find_path(self, start, target):
        queue = deque([[start]])
        visited = {start}
        while queue:
            path = queue.popleft()
            current = path[-1]
            if current == target:
                return path
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None

    def find_all_reachable(self, start):
        # TASK 3: build this using DFS
        # Goal: return a set of every node reachable from `start`
        pass


# --- Build the network ---
net = Graph()
net.add_edge("Attacker_Laptop", "Guest_WiFi")
net.add_edge("Guest_WiFi", "Reception_PC")
net.add_edge("Reception_PC", "File_Server")
net.add_edge("File_Server", "Domain_Controller")
net.add_edge("Guest_WiFi", "Printer")

print(net.find_path("Attacker_Laptop", "Domain_Controller"))
print(net.find_all_reachable("Attacker_Laptop"))