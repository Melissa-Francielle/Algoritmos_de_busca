from collections import deque 
import sys 
def hanoi(n, source, target, auxiliary):
    if n == 1:
        return
    else:
        hanoi(n - 1, source, auxiliary, target)

        hanoi(n - 1, auxiliary, target, source)


def hanoi_bfs(n):
    initial_state = (tuple(range(n, 0, -1)), (), ())
    goal_state = ((), (), tuple(range(n, 0, -1)))

    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        A, B, C = current_state
        towers = [A, B, C]
        
        for i in range(3):
            for j in range(3):
                if i != j and towers[i]:
                    new_towers = [list(towers[0]), list(towers[1]), list(towers[2])]
                    disk = new_towers[i].pop()
                    if not new_towers[j] or new_towers[j][-1] > disk:
                        new_towers[j].append(disk)
                        new_state = tuple(map(tuple, new_towers))
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_state, path + [(disk, i, j)]))



def hanoi_dijkstra(n):
    initial_state = (tuple(range(n, 0, -1)), (), ())
    goal_state = ((), (), tuple(range(n, 0, -1)))

    queue = deque([(initial_state, 0)])  # Estado inicial com distância 0
    distances = {initial_state: 0}
    parents = {initial_state: None}
    
    while queue:
        current_state, current_distance = queue.popleft()
        
        if current_state == goal_state:
            break
        
        A, B, C = current_state
        towers = [A, B, C]
        
        for i in range(3):
            for j in range(3):
                if i != j and towers[i]:
                    new_towers = [list(towers[0]), list(towers[1]), list(towers[2])]
                    disk = new_towers[i].pop()
                    if not new_towers[j] or new_towers[j][-1] > disk:
                        new_towers[j].append(disk)
                        new_state = tuple(map(tuple, new_towers))
                        new_distance = current_distance + 1
                        if new_state not in distances or new_distance < distances[new_state]:
                            distances[new_state] = new_distance
                            parents[new_state] = (current_state, (disk, i, j))
                            queue.append((new_state, new_distance))
    
    # Reconstrução do caminho
    path = []
    state = goal_state
    while state != initial_state:
        state, move = parents[state]
        path.append(move)
    
    path.reverse()
    return path

def hanoi_dfs(n):
    initial_state = (tuple(range(n, 0, -1)), (), ())
    goal_state = ((), (), tuple(range(n, 0, -1)))
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        current_state, path = stack.pop()
        
        if current_state == goal_state:
            return path
        
        if current_state in visited:
            continue
        
        visited.add(current_state)
        
        A, B, C = current_state
        towers = [A, B, C]
        
        for i in range(3):
            for j in range(3):
                if i != j and towers[i]:
                    new_towers = [list(towers[0]), list(towers[1]), list(towers[2])]
                    disk = new_towers[i].pop()
                    if not new_towers[j] or new_towers[j][-1] > disk:
                        new_towers[j].append(disk)
                        new_state = tuple(map(tuple, new_towers))
                        if new_state not in visited:
                            stack.append((new_state, path + [(disk, i, j)]))

def hanoi_iddfs(n):
    initial_state = (tuple(range(n, 0, -1)), (), ())
    goal_state = ((), (), tuple(range(n, 0, -1)))

    def dls(state, depth, visited, path):
        if state == goal_state:
            return path
        if depth == 0:
            return None
        
        A, B, C = state
        towers = [A, B, C]
        
        for i in range(3):
            for j in range(3):
                if i != j and towers[i]:
                    new_towers = [list(towers[0]), list(towers[1]), list(towers[2])]
                    disk = new_towers[i].pop()
                    if not new_towers[j] or new_towers[j][-1] > disk:
                        new_towers[j].append(disk)
                        new_state = tuple(map(tuple, new_towers))
                        if new_state not in visited:
                            visited.add(new_state)
                            result = dls(new_state, depth - 1, visited, path + [(disk, i, j)])
                            if result is not None:
                                return result
                            visited.remove(new_state)
        return None
    
    # Executando a busca em profundidade iterativa
    for depth_limit in range(1, n + 1):  # Limites de profundidade de 1 a n
        visited = set([initial_state])
        result = dls(initial_state, depth_limit, visited, [])
        if result is not None:
            return result
    return None

def hanoi_dls(n, limit):
    initial_state = (tuple(range(n, 0, -1)), (), ())
    goal_state = ((), (), tuple(range(n, 0, -1)))

    def dls(state, depth, visited, path):
        if state == goal_state:
            return path
        if depth == 0:
            return None
        
        A, B, C = state
        towers = [A, B, C]
        
        for i in range(3):
            for j in range(3):
                if i != j and towers[i]:
                    new_towers = [list(towers[0]), list(towers[1]), list(towers[2])]
                    disk = new_towers[i].pop()
                    if not new_towers[j] or new_towers[j][-1] > disk:
                        new_towers[j].append(disk)
                        new_state = tuple(map(tuple, new_towers))
                        if new_state not in visited:
                            visited.add(new_state)
                            result = dls(new_state, depth - 1, visited, path + [(disk, i, j)])
                            if result is not None:
                                return result
                            visited.remove(new_state)
        return None
    
    visited = set([initial_state])
    return dls(initial_state, limit, visited, [])

def main():

    n = 5  # Número de discos
    move = hanoi(n, 'Torre 1 ', 'Torre 2', 'Torre 3')

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
            print("\nExiting...\n\tGoodbye")
            exit(1)
        elif op == 1:
            path = hanoi_bfs(n)
            if path:
                print("\n\t------Resultado gerado (BFS)------")
                for move in path:
                    disk, src, dest = move
                    print(f"Mova o disco {disk} de {src} para {dest}")
            else:
                print("\n\t------Nenhum caminho encontrado (BFS)------")
        elif op == 2:
            path = hanoi_dijkstra(n)
            if path:
                print("\n\t------Resultado gerado (Dijkstra)------")
                for move in path:
                    disk, src, dest = move
                    print(f"Mova o disco {disk} de {src} para {dest}")
            else:
                print("\n\t------Nenhum caminho encontrado (Dijkstra)------")
        elif op == 3:
            path = hanoi_dfs(n)
            if path:
                print("\n\t------Resultado gerado (DFS)------")
                for move in path:
                    disk, src, dest = move
                    print(f"Mova o disco {disk} de {src} para {dest}")
            else:
                print("\n\t------Nenhum caminho encontrado (DFS)------")
        elif op == 4:
            path = hanoi_iddfs(n)
            if path:
                print("\n\t------Resultado gerado (Iterative Depth)------")
                for move in path:
                    disk, src, dest = move
                    print(f"Mova o disco {disk} de {src} para {dest}")
            else:
                print("\n\t------Nenhum caminho encontrado (DFS Iterative)------")
        elif op == 5:
            limit = int(input("\nDigite um limite para esse algoritmo: "))
            path = hanoi_dls(n, limit)
            if path:
                print("\n\t--------Resultado gerado (Limited Depth)-----------")
                for move in path:
                    disk, src, dest = move
                    print(f"Mova o disco {disk} de {src} para {dest}")
        else:
            print("\nINVALID")
            exit(1)
                
if __name__ == "__main__":
    main()


