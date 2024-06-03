using System;
using System.Collections.Generic;
using System.Linq;

class Program{
    static List<string> Dls(Dictionary<string, List<string>> graph, string start, string finish, int limit){
        var visited = new HashSet<string>();
        var path = new List<string>();
        if (DlsRecursive(graph, start, finish, visited, path, 0, limit)){
            return path;
        }
        else{ return null; }
    }

    static bool DlsRecursive(Dictionary<string, List<string>> graph, string current, string finish, HashSet<string> visited, List<string> path, int depth, int limit){
        if (depth <= limit){
            visited.Add(current);
            path.Add(current);
            Console.WriteLine("Visitando nó: " + current + ", Profundidade: " + depth);

            if (current == finish)
                return true;

            foreach (var neighbor in graph[current]){
                if (!visited.Contains(neighbor)){
                    if (DlsRecursive(graph, neighbor, finish, visited, path, depth + 1, limit))
                        return true;
                }
            }

            path.RemoveAt(path.Count - 1);
        }
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
        var startCity = Console.ReadLine();
        Console.WriteLine("\nDigite a cidade final: ");
        var finishCity = Console.ReadLine();

        Console.WriteLine("\nDigite a profundidade máxima: ");
        int limit = int.Parse(Console.ReadLine());

        var path = Dls(graph, startCity, finishCity, limit);
        if (!graph.ContainsKey(startCity) || !graph.ContainsKey(finishCity)){
            Console.WriteLine("\nCidade não encontrada, por favor tente novamente");
        }
        else
        {
            if (path != null){
                Console.WriteLine("Caminho encontrado: " + string.Join(" -> ", path));

            }
            else
            {
                Console.WriteLine("Não há caminho possível.");
            }
        }
    }
}
