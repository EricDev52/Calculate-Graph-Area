import tkinter as tk
from math import *

window = tk.Tk()   # Start Tkinter

window.title("Calculate Graph")

canvas = tk.Canvas(window, width=400, height=400)   # Tkinter window size
canvas.pack()
canvas.create_rectangle(50, 50, 350, 350, fill='#cccccc')

def f(x):   # for calculate point in function  and replace so that you can write x^2 instead of x**2
    if x == 0: return 0 # To avoid division by zero
    else: return eval((fInput.get().replace(",",".")).replace("^","**"))

canvas.create_text((25, 15), text="Enter a: ")   #Input windows
canvas.create_text((25, 35), text="Enter b: ")
canvas.create_text((202, 15), text="Enter f(x): ")
aInput = tk.Entry (window)
canvas.create_window(110, 15, window=aInput)
bInput = tk.Entry (window) 
canvas.create_window(110, 35, window=bInput)
fInput = tk.Entry (window) 
canvas.create_window(290, 15, window=fInput)

TempCanvas = []  # For deleting specific canvas elements when calculating new graph

def CalculateGraph(a,b):
    for TempCanvasElement in TempCanvas:
        canvas.delete(TempCanvasElement)
    A=0
    n=100000  # Number of square that were placed inside the graph to calculate the area
    HeighestPoint = 0
    LowestPoint = 0
    for i in range(n):
        A += (((b-a)/n)*abs(f(a+((b-a)/n)*i))) # Calculate Area
    for i in range(10000):
        if i == 0:
            HeighestPoint = f(a+((b-a)/10000)*i)      # Check for highest and lowest point in graph
            LowestPoint = f(a+((b-a)/10000)*i)
        else:
            if f(a+((b-a)/10000)*i) > HeighestPoint:
                HeighestPoint = f(a+((b-a)/10000)*i)
            if f(a+((b-a)/10000)*i) < LowestPoint:
                LowestPoint = f(a+((b-a)/10000)*i)
    Height = HeighestPoint - LowestPoint   # Height of graph from top to bottom
    if Height == 0:  # if you input as example y=5 then the heighest and lowest point is to same to display this we just set one of this values to 0
        if HeighestPoint > 0:
            LowestPoint = 0
        elif HeighestPoint < 0:
            HeighestPoint = 0
        Height = HeighestPoint - LowestPoint
    for i in range(1000):
        if round(HeighestPoint,1) >= 0 and round(LowestPoint,1) <= 0:   # Only paint 1000 lines that will make up the area if the x-axis from which out the line will be painted is inside the window
            TempCanvas.append(canvas.create_line((300/1000*i+50,(300-((0-LowestPoint)/Height*300)+50)),(300/1000*i+50,(300-((f(a+((b-a)/1000)*i)-LowestPoint)/Height*300)+50)),fill="#e3645b")) # Paint Area
        elif round(HeighestPoint,1) < 0:  # otherwise just make the graph from top or bottom of the window 
            TempCanvas.append(canvas.create_line((300/1000*i+50,50),(300/1000*i+50,(300-((f(a+((b-a)/1000)*i)-LowestPoint)/Height*300)+50)),fill="#e3645b")) # Paint Area
        elif round(LowestPoint,1) > 0:
            TempCanvas.append(canvas.create_line((300/1000*i+50,350),(300/1000*i+50,(300-((f(a+((b-a)/1000)*i)-LowestPoint)/Height*300)+50)),fill="#e3645b")) # Paint Area
        TempCanvas.append(canvas.create_text((300/1000*i+50, (300-((f(a+((b-a)/1000)*i)-LowestPoint)/Height*300)+48)), text=".")) # Display Graph with 1000 text dots (.) on the right position
    if round(HeighestPoint,1) >= 0 and round(LowestPoint,1) <= 0:   # Display x- and y- axis on the right position scaled to the window  if the x-axis and y-axis is inside the window
        TempCanvas.append(canvas.create_line((50,(300-((0-LowestPoint)/Height*300)+50)),(350,(300-((0-LowestPoint)/Height*300)+50)), fill="#2132cf", width=2)) # X-Axis
    if round(b,1) >= 0 and round(a,1) <= 0:
        TempCanvas.append(canvas.create_line(((((0-a)/(b-a)*300)+50),50),((((0-a)/(b-a)*300)+50),350), fill="#2132cf", width=2)) # Y-Axis
    TempCanvas.append(canvas.create_text((200, 40), text=round(HeighestPoint,3)))   # Display text on the side, bottom and top of the window
    TempCanvas.append(canvas.create_text((35, 200), text=round(a,3)))
    TempCanvas.append(canvas.create_text((365, 200), text=round(b,3)))
    TempCanvas.append(canvas.create_text((200, 360), text=round(LowestPoint,3)))
    TempCanvas.append(canvas.create_text((200, 390), text="A = " + str(round(A,3)) + " cm²"))


def TestInput():   # Test if inputed value works to diplay
    try:
        if aInput.get() == "" or bInput.get() == "" or fInput.get() == "":
            for Element in TempCanvas:
                canvas.delete(Element)
            TempCanvas.append(canvas.create_text((200, 40), text="Fill all"))
        elif float(aInput.get().replace(",",".")) >= float(bInput.get().replace(",",".")):
            for Element in TempCanvas:
                canvas.delete(Element)
            TempCanvas.append(canvas.create_text((200, 40), text="a not < b"))
        elif ("x" not in fInput.get() and eval(fInput.get()) == 0):
            for Element in TempCanvas:
                canvas.delete(Element)
            TempCanvas.append(canvas.create_text((200, 390), text="A = 0 cm²"))
        else:
            for Element in TempCanvas:
                canvas.delete(Element)
            CalculateGraph(float(aInput.get().replace(",",".")),float(bInput.get().replace(",",".")))
    except:   # Otherwise show an error text
        for Element in TempCanvas:
            canvas.delete(Element)
        TempCanvas.append(canvas.create_text((200, 40), text="Error"))

def enter(event):
    TestInput()
window.bind("<Return>", enter)  # So that we can also calculate on enter key
CalculateButton = tk.Button(text='Calculate (Enter)', command=TestInput)   # Display Calculate button and on click do TestInput () function
canvas.create_window(303, 35, window=CalculateButton)

window.mainloop()   # Mainloop for tkinter
