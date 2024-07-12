def calculate_amount(graph):
    n = len(graph)
    amount = [0] * n

    for p in range(n):
        for i in range(n):
            amount[p] += (graph[i][p] - graph[p][i])

    return amount

def get_min_index(arr):
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

def get_max_index(arr):
    max_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

def min_of_2(x, y):
    return x if x < y else y