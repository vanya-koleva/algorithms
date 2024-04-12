def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


some_list = [int(x) for x in input().split()]
searched_item = int(input())
idx = binary_search(some_list, searched_item)
print(f"Searched item's index: {idx}")
