import heapq

# Defining the function to load the graph from the external file
def load_graph(file_name):
    graph = {}
    with open(file_name, 'r') as file:
        for line in file:
            nodes = line.strip().split()
            node1, node2, weight = nodes
            weight = int(weight)
            if node1 not in graph:
                graph[node1] = {}
            graph[node1][node2] = weight
            if node2 not in graph:
                graph[node2] = {}
    return graph

# Defining the function to find the shortest path using Dijkstra's algorithm
def shortest_path(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    paths = {start: []}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                paths[adjacent] = paths[current_node] + [adjacent]
                heapq.heappush(queue, (distance, adjacent))

    if end not in paths:
        return None, None

    return distances[end], paths[end]

# Defining the function to recommend the most efficient route
def recommend_route(graph, start, charging_stations):
    shortest_paths = {station: shortest_path(graph, start, station) for station in charging_stations}
    shortest_distances = {station: dist for station, (dist, _) in shortest_paths.items() if dist is not None}
    recommended_station = min(shortest_distances, key=shortest_distances.get)
    return recommended_station, shortest_paths[recommended_station]

# Loading the graph from the external file
graph = load_graph('graph.txt')

# Defining the charging stations
charging_stations = ['H', 'K', 'Q', 'T']

# Getting user input for the starting node
start = input("Enter the starting node: ").upper()

# Recommending the most efficient route
recommended_station, (distance, path) = recommend_route(graph, start, charging_stations)
if recommended_station:
    print(f"The most efficient route from {start} to a charging station is to {recommended_station} with a total distance of {distance}. The path is {path}.")
else:
    print(f"There is no route from {start} to any of the charging stations.")