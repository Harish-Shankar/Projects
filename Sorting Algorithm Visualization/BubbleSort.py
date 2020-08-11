import time


def bubble_sort(nums, draw_data):
    for _ in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                draw_data(nums, ['orange' if x == j or x == j+1 else 'red' for x in range(len(nums))])
                time.sleep(0.5)
    draw_data(nums, ['green' for i in range(len(nums))])
