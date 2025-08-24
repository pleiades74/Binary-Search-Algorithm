
```python
def binary_search(arr, target):
    """
    Perform binary search on a sorted list.
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Middle index
        guess = arr[mid]

        if guess == target:
            return mid  # Found the target
        elif guess < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 15, 20]
    target = 7
    result = binary_search(numbers, target)

    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the list")
