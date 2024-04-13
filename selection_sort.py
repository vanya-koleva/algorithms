def selection_sort(lst: list[int], n: int) -> list[int]:
    for i in range(n - 1):
        smallest = i

        for j in range(i + 1, n):
            if lst[j] < lst[smallest]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]

    return lst


some_list = [12, 9, 3, 7, 14, 11]
num = len(some_list)
print(selection_sort(some_list, num))
