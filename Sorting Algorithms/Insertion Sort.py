import random


def insertion_sort(arr):
    for num in range(1, len(arr)):
        val = arr[num]
        while arr[num-1] > val and num>0:
            arr[num], arr[num-1] = arr[num-1], arr[num]
            num -= 1
    return arr


def main():
    arr = random.sample(range(1, 50), 10)
    print(arr)
    print(insertion_sort(arr))


main()
