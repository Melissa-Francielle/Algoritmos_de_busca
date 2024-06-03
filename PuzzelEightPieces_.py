from collections import deque
import heapq

tamanho_quebraCabeca = 3

def printMatrix(path): #imprimir o caminho 
    for state in path:
        for row in state:
            print(row)
        print()

def get_neighbors(state):
    neighbors = []
    empty_tile = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]
    x, y = empty_tile

    directions = {
        'up': (x - 1, y),
        'down': (x + 1, y),
        'left': (x, y - 1),
        'right': (x, y + 1)
    }

    for direction, (new_x, new_y) in directions.items():
        if 0 <= new_x < tamanho_quebraCabeca and 0 <= new_y < tamanho_quebraCabeca:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def _bfs(initial, end):
    visited = set()
    queue = deque([(initial, [])])

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path + [node]
        if str(node) not in visited:
            visited.add(str(node))
            for neighbor in get_neighbors(node):
                queue.append((neighbor, path + [node]))

    return []

def _dfs(initial, end):
    visited = set()
    stack = [(initial, [])]

    while stack:
        current, path = stack.pop()
        if current == end:
            return path + [current]
        if str(current) not in visited:
            visited.add(str(current))
            for neighbor in get_neighbors(current):
                stack.append((neighbor, path + [current]))

    return []

def _depthLimited(initial, end, limit):
    visited = set()
    path = []
    result = limited_recursive(initial, end, visited, path, 0, limit)
    return path if result else []

def limited_recursive(current, end, visited, path, depth, limit):
    if depth > limit:
        return False
    
    visited.add(str(current))
    path.append(current)

    if current == end:
        return True

    for neighbor in get_neighbors(current):
        if str(neighbor) not in visited:
            if limited_recursive(neighbor, end, visited, path, depth + 1, limit):
                return True

    path.pop()
    return False

def _depthIterative(initial, end):
    limit = 1
    while True:
        path = _depthLimited(initial, end, limit)
        if path:
            return path
        limit += 1

def _dijkstra(initial, end):
    queue = [(0, initial)]
    visited = set()
    parents = {str(initial): None}
    distances = {str(initial): 0}

    while queue:
        current_distance, current_state = heapq.heappop(queue)
        visited.add(str(current_state))

        if current_state == end:
            break
            
        for neighbor in get_neighbors(current_state):
            neighbor_str = str(neighbor)
            if neighbor_str not in visited:
                new_distance = current_distance + 1  # Distance between nodes is constant (1)
                if new_distance < distances.get(neighbor_str, float('inf')):
                    distances[neighbor_str] = new_distance
                    parents[neighbor_str] = current_state
                    heapq.heappush(queue, (new_distance, neighbor))

    path = []
    current_state = end
    while current_state is not None:
        path.append(current_state)
        current_state = parents[str(current_state)]
    path.reverse()

    return path

def main():
    initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
    final = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
    
    print("\n\t--------------Matriz Inicial-----------------\n")
    printMatrix(initial)
    print("\n")

    while True:
        print("\n\t------- OPCOES DE ALGORITMOS -------")
        menu = """
        0 - Sair
        1 - BFS 
        2 - Dijkstra
        3 - DFS
        4 - Depth Iterative
        5 - Depth Limited
        """
        print(menu)
        
        op = int(input("\nInforme qual algoritmo gostaria de executar: "))
        
        if op == 0:
            print("\nSaindo...\n\tADEUS")
            break
        elif op == 1:
            path = _bfs(initial, final)
            if path:
                print("\n\t------Resultado gerado (BFS)------")
                printMatrix(path)
            else:
                print("\n\t------Nenhum caminho encontrado (BFS)------")
        elif op == 2:
            path = _dijkstra(initial, final)
            if path:
                print("\n\t------Resultado gerado (Dijkstra)------")
                printMatrix(path)
            else:
                print("\n\t------Nenhum caminho encontrado (Dijkstra)------")
        elif op == 3:
            path = _dfs(initial, final)
            if path:
                print("\n\t------Resultado gerado (DFS)------")
                printMatrix(path)
            else:
                print("\n\t------Nenhum caminho encontrado (DFS)------")
        elif op == 4:
            path = _depthIterative(initial, final)
            if path:
                print("\n\t------Resultado gerado (Depth Iterative)------")
                printMatrix(path)
            else:
                print("Invalid Number")
if __name__ == "__main__":
    main()
