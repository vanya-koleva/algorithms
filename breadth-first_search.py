from collections import deque


graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G", "H"],
    "D": ["F"],
    "E": [],
    "F": [],
    "G": [],
    "H": []
}


def searched_criteria(name):
    return name == "N"


def search(node):
    search_queue = deque()
    search_queue += node
    visited = []

    while search_queue:
        person = search_queue.popleft()
        print(f"Current node: {person}")

        if person not in visited:
            if searched_criteria(person):
                print(f"{person} found")
                return True
            else:
                search_queue += graph[person]
                visited.append(person)

    print("Not found")
    return False


search("A")
