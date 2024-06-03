using System;
using System.Collections.Generic;
class Program
{
    static List<string> Interative(Dictionary<string, List<string>> graph, string start, string finish){
        for (int limit = 1; ; limit++){
            var visited = new HashSet<string>();
            var path = new List<string>();
            Console.WriteLine("\n\tTENTANDO COM A PROFUNDIDADE LIMITE: " + limit);

            if (Recursive(graph, start, finish, visited, path, 0, limit)){
                return path;
            }
        }
    }

    static bool Recursive(Dictionary<string, List<string>> graph, string current, string finish, HashSet<string> visited, List<string> path, int depth, int limit){
        if (depth > limit){
            return false;
        }

        visited.Add(current);
        path.Add(current);
        Console.WriteLine("\nVisitando nó: " + current + ", Profundidade: " + depth);

        if (current == finish){
            return true;
        }

        foreach (var neighbor in graph[current]){
            if (!visited.Contains(neighbor)){
                if (Recursive(graph, neighbor, finish, visited, path, depth + 1, limit)){
                    return true;
                }
            }
        }

        path.RemoveAt(path.Count - 1);
        visited.Remove(current);
        return false;
    }

    static void Main(string[] args){
        var graph = new Dictionary<string, List<string>>(){
            { "Arad", new List<string> { "Sibiu", "Timisoara", "Zerind" } },
            { "Zerind", new List<string> { "Arad", "Oradea" } },
            { "Sibiu", new List<string> { "Arad", "Fagaras", "Oradea", "Rimnicu Vilcea" } },
            { "Oradea", new List<string> { "Zerind", "Sibiu" } },
            { "Timisoara", new List<string> { "Arad", "Lugoj" } },
            { "Lugoj", new List<string> { "Timisoara", "Mehadia" } },
            { "Mehadia", new List<string> { "Lugoj", "Drobeta" } },
            { "Drobeta", new List<string> { "Mehadia", "Craiova" } },
            { "Craiova", new List<string> { "Drobeta", "Rimnicu Vilcea", "Pitesti" } },
            { "Rimnicu Vilcea", new List<string> { "Sibiu", "Pitesti", "Craiova" } },
            { "Fagaras", new List<string> { "Sibiu", "Bucharest" } },
            { "Pitesti", new List<string> { "Rimnicu Vilcea", "Craiova", "Bucharest" } },
            { "Bucharest", new List<string> { "Fagaras", "Pitesti", "Giurgiu", "Urziceni" } },
            { "Giurgiu", new List<string> { "Bucharest" } },
            { "Urziceni", new List<string> { "Bucharest", "Hirsova", "Vaslui" } },
            { "Hirsova", new List<string> { "Urziceni", "Eforie" } },
            { "Eforie", new List<string> { "Hirsova" } },
            { "Vaslui", new List<string> { "Urziceni", "Iasi" } },
            { "Iasi", new List<string> { "Vaslui", "Neamt" } },
            { "Neamt", new List<string> { "Iasi" } }
        };

        Console.WriteLine("Digite a cidade inicial: ");
        var starting = Console.ReadLine();
        Console.WriteLine("\nDigite a cidade final: ");
        var goal = Console.ReadLine();

        var path = Interative(graph, starting, goal);

        if (!graph.ContainsKey(starting) || !graph.ContainsKey(goal)){
            Console.WriteLine("\nCidade não encontrada, por favor tente novamente");
        }
        else
        {
            if (path != null){
                Console.WriteLine("\nCAMINHO ENCONTRADO: " + string.Join(" -> ", path));
            }
            else{
                Console.WriteLine("Não há caminho possível.");
            }
        }
    }
}
