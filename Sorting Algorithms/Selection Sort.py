import random


def selection_sort(arr):
    for num in range(len(arr)-1):
        minValue = num
        for j in range(num+1, len(arr)):
            if arr[j] < arr[minValue]:
                minValue = j
        if minValue != num:
            arr[minValue], arr[num] = arr[num], arr[minValue]

    return arr


def main():
    arr = random.sample(range(1, 50), 10)
    print(arr)
    print(selection_sort(arr))


main()
