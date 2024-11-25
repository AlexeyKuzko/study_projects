def quicksort_depth(arr, depth):
    if len(arr) <= 1:
        return depth

    mid_index = (len(arr) - 1) // 2
    pivot = arr[mid_index]
    
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    left_depth = quicksort_depth(less, depth + 1)
    right_depth = quicksort_depth(greater, depth + 1)
    
    return max(left_depth, right_depth)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    max_depth = quicksort_depth(arr, 0)
    print(max_depth)