import random


def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]
        merge_sort(left)
        merge_sort(right)
        fin = []
        leftI = rightI = mainI = 0

        while leftI < len(left) and rightI < len(right):
            if left[leftI] < right[rightI]:
                arr[mainI] = left[leftI]
                leftI += 1
            else:
                arr[mainI] = right[rightI]
                rightI += 1
            mainI += 1
        while leftI < len(left):
            arr[mainI] = left[leftI]
            leftI += 1
            mainI += 1
        while rightI < len(right):
            arr[mainI] = right[rightI]
            rightI += 1
            mainI += 1
    return arr


def main():
    arr = random.sample(range(1, 50), 10)
    print(arr)
    print(merge_sort(arr))


main()
