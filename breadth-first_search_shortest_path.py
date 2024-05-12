from collections import deque


def search(graph: dict, start: str, goal: str):
    search_queue = deque()
    search_queue += start
    visited = []

    if start == goal:
        print("Start = goal")
        return [start]

    while search_queue:
        path = search_queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                search_queue.append(new_path)

                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return new_path

            visited.append(node)

    print("Not found")
    return False


graph = {"A": ["B", "C", "E"],
         "B": ["A","D", "E"],
         "C": ["A", "F", "G"],
         "D": ["B"],
         "E": ["A", "B","D"],
         "F": ["C"],
         "G": ["C"]
         }

search(graph, "A", "G")
