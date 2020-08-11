from tkinter import *
from tkinter import ttk
from BubbleSort import bubble_sort
import numpy as np
import random


# Creates the Tkinter Window
root = Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)
root.config(bg='Black')

selectedAlg = StringVar()
nums = []


def draw_data(nums, colors):
    canvas.delete("all")
    # Initializes certain variables that will be used to create the bars
    winHeight = 380
    winWidth = 600
    subWidth = winWidth / (len(nums)+1)
    offset = 30
    spacing = 10

    # Normalizes the data (0 to 1) to make bar's height relative to all the numbers
    normalizedNums = nums / np.linalg.norm(nums)

    for i, height in enumerate(normalizedNums):
        # Initializes the max and min pixels of each bar
        topX = i * subWidth + offset + spacing
        topY = winHeight - height * 375
        bottomX = (i+1) * subWidth + offset
        bottomY = winHeight

        # Creates the bar with the number on the top
        canvas.create_rectangle(topX, topY, bottomX, bottomY, fill=colors[i])
        canvas.create_text(topX+2, topY, anchor=SW, text=str(nums[i]))
    root.update_idletasks()


def generate():
    global nums
    # Retrieves the data filled in
    try:
        sizeVal = int(size.get())
    except:
        sizeVal = 10
    try:
        minVal = int(minNum.get())
    except:
        minVal = 1
    try:
        maxVal = (int(maxNum.get())) + 1
    except:
        maxVal = 500

    # Checks if the data filled in makes sense
    if minVal < 0: minVal = 0
    if maxVal > 500: maxVal = 500
    if sizeVal > 30 or sizeVal < 4: sizeVal = 15
    if minVal > maxVal: minVal, maxVal = maxVal, minVal

    nums = []
    # Creates the random number that will be sorted
    for _ in range(sizeVal):
        nums.append(random.randint(minVal, maxVal))

    draw_data(nums, ['red' for i in range(len(nums))])


def start():
    global nums
    bubble_sort(nums, draw_data)


# Creates a grey area where all the interaction happens
UIFrame = Frame(root, width=600, height=200, bg='Grey')
UIFrame.grid(row=0, column=0, padx=10, pady=5)

# Creates a white area where the visualization will occur
canvas = Canvas(root, width=600, height=380)
canvas.grid(row=1, column=0, padx=10, pady=5)

# Creates a drop-down box to chose the algorithm
Label(UIFrame, text='Algorithm', bg='Grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UIFrame, textvariable=selectedAlg, values=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

# Creates a button when clicked will start the visualization process
Button(UIFrame, text='Start', command=start, bg='red').grid(row=0, column=2, padx=5, pady=5)

# Creates a box where the user can enter the number of number to be sorted
Label(UIFrame, text='Size', bg='Grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
size = Entry(UIFrame)
size.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# Creates a box where the user can enter the minimum a number can be
Label(UIFrame, text='Minimum', bg='Grey').grid(row=1, column=2, padx=5, pady=5, sticky=W)
minNum = Entry(UIFrame)
minNum.grid(row=1, column=3, padx=5, pady=5, sticky=W)

# Creates a box where the user can enter the maximum a number can be
Label(UIFrame, text='Maximum', bg='Grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxNum = Entry(UIFrame)
maxNum.grid(row=1, column=5, padx=5, pady=5, sticky=W)

# Creates a randomized assortment of numbers within the given range
Button(UIFrame, text='Generate', command=generate, bg='White').grid(row=1, column=6, padx=5, pady=5)


root.mainloop()
