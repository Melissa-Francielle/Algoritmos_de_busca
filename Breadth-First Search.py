from collections import deque

def bfs(graph, start, finish):
    visited = set()
    queue = deque([(start, [start])])  

    while queue:
        node, path = queue.popleft() 
        if node == finish:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))                    

graph = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Zerind': ['Arad', 'Oradea'],
    'Sibiu': ['Arad', 'Fagaras', 'Oradea', 'Rimnicu Vilcea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']

}
start_city= input ("Informe a cidade: ")
finish_city = input("Informe a cidade final: ")

if start_city not in graph or finish_city not in graph:
    print("Cidade não encontrada por favor tente novamete!")
else:
    path = bfs(graph, start_city, finish_city)
    if path:
        print("Caminho encontrado:", ' -> '.join(path))
    else:
        print("Não há caminho possivel")


