from collections import deque
import sys

def dijkstra(graph, start, finish):
    queue = deque([(start, 0)])  # Incluindo o peso inicial como 0 para a cidade de origem
    visited = set()
    parents = {city: None for city in graph}
    distances = {city: sys.maxsize for city in graph}
    distances[start] = 0

    while queue:
        current_city, current_distance = queue.popleft()
        visited.add(current_city)

        if current_city == finish:
            break

        for neighbor, edge_distance in graph[current_city].items():
            if neighbor not in visited:
                new_distance = current_distance + edge_distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    parents[neighbor] = current_city
                    queue.append((neighbor, new_distance))

    path = []
    current_city = finish
    total_distance = distances[finish]
    while current_city is not None:
        path.append((current_city, distances[current_city]))
        current_city = parents[current_city]
    path.reverse()

    return path[1:], total_distance  # Excluir a cidade de origem do caminho

# Grafo com pesos das arestas
graph = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu Vilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

def print_path_with_distances(path):
    current_distance = 0
    for city, dist in path:
        print(city, "(Distância:", dist - current_distance, ") -> ", end="")
        current_distance = dist
    print()

start_city = input("Informe a cidade de origem: ")
finish_city = input("Informe a cidade de destino: ")

if start_city not in graph or finish_city not in graph:
    print("Cidade não encontrada, por favor, tente novamente!")
else:
    path, total_distance = dijkstra(graph, start_city, finish_city)
    if path:
        print("Caminho encontrado:")
        print_path_with_distances(path)
        print("Distância total:", total_distance)
    else:
        print("Não há caminho possível.")
