def binary_search(nums: list[int], target_num: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle_index = (low + high) // 2
        middle_element = nums[middle_index]
        if middle_element == target_num:
            return middle_index
        if middle_element > target_num:
            high = middle_index - 1
        else:
            low = middle_index + 1


numbers = [int(x) for x in input().split(", ")]
searched_num = int(input())
result = binary_search(numbers, searched_num)
print(f"Target number index: {result}")
