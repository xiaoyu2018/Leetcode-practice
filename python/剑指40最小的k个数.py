
def getLeastNumbers(arr: list, k: int) -> list:
    return sorted(arr)[:k]


from heapq import *
def getLeastNumbers(arr: list, k: int) -> list:
    heapify(arr)
    return [heappop(arr) for _ in range(k)]