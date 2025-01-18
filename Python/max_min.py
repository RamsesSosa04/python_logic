"""
  Finds the maximum and minimum values in a list of integers.

  Args:
    numbers: A list of integers.

  Returns:
    The maximum and minimum integers in the list.
"""
def minimum(arr):
    min_value = arr[0]
    for num in arr[1:]:
        if num < min_value:
            min_value = num
    return min_value

def maximum(arr):
    max_value = arr[0]
    for num in arr[1:]:
        if num > max_value:
            max_value = num
    return max_value
list = [4, 6, 2, 1, 9, 63, -134, 566]
min_value = minimum(list)
max_value = maximum(list)
print(f"Min: {min_value}, Max: {max_value}")