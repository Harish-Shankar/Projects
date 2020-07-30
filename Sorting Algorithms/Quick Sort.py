import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
    greaterThan = []
    lessThan = []

    for num in arr:
        if num > pivot:
            greaterThan.append(num)
        else:
            lessThan.append(num)
    return quick_sort(lessThan) + [pivot] + quick_sort(greaterThan)


def main():
    arr = random.sample(range(1, 50), 10)
    print(arr)
    print(quick_sort(arr))


main()
