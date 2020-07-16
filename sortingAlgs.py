from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root = Tk()
root.title('Algo Visualizer: Kevin John, Joshua Pierre, Ashely Tucker, Sean Moon')
root.maxsize(1800, 1000)
root.config(bg='gray')

#variables
selectedAlg = StringVar()
data = []
speed = .2
algMessage = ''

#function
def drawGraph(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 1000
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    root.update()


def Generate():
    global data
    
    if minEntry.get() == '':
        minVal = 0
    else:
        minVal = int(minEntry.get())

    if maxEntry.get() == '':
        maxVal = 10
    else:
        maxVal = int(maxEntry.get())
    
    if sizeEntry.get() == '':
        size = 10
    else:
        size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawGraph(data, ['blue' for x in range(len(data))]) #['red', 'red' ,....]

def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawGraph, speed)
        algMessage = 'Quick Sort    Avg Case: n*log(n)     Best Case: n*log(n)   Worst Case: n^2'
    
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawGraph, speed)
        algMessage = 'Bubble Sort    Avg Case: n^2    Best Case: n^2    Worst Case: n^2'

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawGraph, speed)
        algMessage = 'Merge Sort    Avg Case: n*log(n)    Best Case: n*log(n)    Worst Case: n*log(n)'

    drawGraph(data, ['green' for x in range(len(data))])


#frame / base lauout
UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=1000, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selectedAlg, values=['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)
Button(UI_frame, text="Generate", command=Generate, bg='red').grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='green').grid(row=0, column=3, padx=5, pady=5)
#Row[1]
Label(UI_frame, text="Size ", bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Min Value ", bg='grey').grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Max Value ", bg='grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)

Label(UI_frame, text, bg='grey').grid(row= 3, column=0, padx=5, pady=5, sticky=W)

root.mainloop()

