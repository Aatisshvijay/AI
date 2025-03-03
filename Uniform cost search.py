//code
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, start, end, cost):
        self.graph.add_edge(start, end, weight=cost)

    def uniform_cost_search(self, start, goal):
        pq = [(0, start, [])]  # (cost, node, path)
        visited = {}

        while pq:
            cost, node, path = heapq.heappop(pq)

            if node in visited and visited[node] <= cost:
                continue
            visited[node] = cost
            path = path + [node]

            if node == goal:
                return path, cost  # Optimal path and its cost

            for neighbor in self.graph.neighbors(node):
                edge_cost = self.graph[node][neighbor]['weight']
                heapq.heappush(pq, (cost + edge_cost, neighbor, path))

        return [], float('inf')  # No valid route found

    def draw_graph(self, path=[]):
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'weight')

        plt.figure(figsize=(6, 6))
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        if path:
            edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(self.graph, pos, edgelist=edges, edge_color='red', width=2)

        plt.title("Uniform Cost Search - Fuel Efficient Route")
        plt.show()

# Example usage
graph = Graph()
graph.add_edge("A", "B", 5)
graph.add_edge("A", "C", 10)
graph.add_edge("B", "D", 15)
graph.add_edge("C", "D", 5)
graph.add_edge("D", "E", 10)

start, goal = "A", "E"
path, cost = graph.uniform_cost_search(start, goal)
print(f"Minimum fuel cost path from {start} to {goal}: {path}, Cost: {cost}")
graph.draw_graph(path)
