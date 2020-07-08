from tkinter import *
from tkinter import ttk
import random
import time

root = Tk()
root.title('Algorithim Visualizor')
root.maxsize(900, 600)
root.config(bg = 'black')

#vars
selected_alg = StringVar()
data = []

#functions
def DrawDataFunction(data: list, highlight = []):
        canvas.delete("all")
        c_height = 300
        c_width = 550
        x_width = c_width / (len(data)+1)
        offset = 30
        spacing =20
        adjusting_ratio = (c_height-30)/ max(data)
        normalizeData = [ i * (adjusting_ratio) for i in data]

        for i, height in enumerate(normalizeData):
                
                #Top left of the rectangle
                x0 = i * x_width + offset + spacing
                y0 = c_height - height
                
                #Bottom right
                x1 = (i+1) * x_width + offset
                y1 = c_height

                if(i in highlight):
                        canvas.create_rectangle(x0,y0,x1,y1, fill = "green")
                else:
                        canvas.create_rectangle(x0,y0,x1,y1, fill = "blue")
                canvas.create_text(x0+2, y0, anchor= SW, text = str(data[i]))
        root.update()

def InsertSort(data: list):
        selected = 0
        solved = []
        for i, value in enumerate(data):
                print(i)
                selected = i
                print (selected)
                while selected!= 0 and data[selected] < data[selected-1]:
                        temp = data[selected-1]
                        data[selected-1] = data[selected]
                        data[selected]= temp
                        solved.append(selected)
                        DrawDataFunction(data, solved)
                        solved.clear()
                        time.sleep(.2)
                                
                        selected -=1

def Generate():
        #Local Vars
        randomizer = random
        size = 0
        min = 0

        data.clear()

        #Setting Local Vars
        if sizeEntry.get() == "":
                size = 10
        else:
                size = int(sizeEntry.get())

        if minEntry.get() == "":
                min = 0
        else:
                min = int(minEntry.get())

        if maxEntry.get() == "":
                max = 10
        else:
                max = int(maxEntry.get())
        
        #Randomizer
        i = 0
        while i < int(size):
                newEntry = randomizer.randrange(min, max, 1)
                data.append(newEntry)
                i+=1
        
        DrawDataFunction(data)
             




def Start():
        print("AlgSelected " + selected_alg.get())   

        InsertSort(data)




#Graph Frame
UI_frame = Frame(root, width = 600, height= 200, bg = "gray" )
UI_frame.grid(row= 0, column= 0, padx= 10, pady= 5)

canvas = Canvas(root, width= 600, height= 380, bg= 'white')
canvas.grid(row= 1, column = 0, padx= 10, pady=5)

#UI area

#Input Area -----------------------------------------------------------------------------------------------
#Row 0 - Algorithim Selection

Label(UI_frame, text= "Algorithim:", bg= 'gray').grid(row=  0, column= 0, padx= 5, sticky= W)
algMenu = ttk.Combobox(UI_frame, textvariable= selected_alg, values=['Insertion Sort','Merge Sort'])
algMenu.grid(row= 0, column= 1, padx= 5)
algMenu.current(0)
Button(UI_frame, text= "Generate", command= Generate, bg = 'blue').grid(row=0, column= 2, padx= 5)
Button(UI_frame, text= "Start", command= Start, bg = 'green').grid(row=0, column= 3, padx= 5)


#Row 1 - Input Specificaiton
Label(UI_frame, text= "Size:", bg= 'gray').grid(row=  1, column= 0, padx= 5, sticky= W)
sizeEntry = Entry(UI_frame) 
sizeEntry.grid(row=  1, column= 1, padx= 5, sticky= W)

Label(UI_frame, text= "Min:", bg= 'gray').grid(row=  1, column= 2, padx= 5, sticky= W)
minEntry = Entry(UI_frame)
minEntry.grid(row=  1, column= 3, padx= 5, sticky= W)

Label(UI_frame, text= "Max:", bg= 'gray').grid(row=  1, column= 4, padx= 5, sticky= W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=  1, column= 5, padx= 5, sticky= W)



root.mainloop()

#Algorithims---------------------------------------------------------------------------------------------
