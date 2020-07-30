import random
from heapq import heappop, heappush


def heap_sort(arr):
    heap = []
    for num in arr:
        heappush(heap, num)
    ordered = []
    while heap:
        ordered.append(heappop(heap))
    return ordered


def main():
    arr = random.sample(range(1, 50), 10)
    print(arr)
    print(heap_sort(arr))


main()
