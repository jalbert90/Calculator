import tkinter as tk

root = tk.Tk()
root.title('root title')
root.geometry("150x150")
root.resizable(False, False)

inpt = tk.Label(root, text="")
inpt.pack()
quitButton = tk.Button(root, text='quit', command=root.destroy)

operators = {"+", "-", "*", "/"}

class Operation:
    def __init__(self):
        self.input = ""
        self.operatorInInput = False
        self.operator = ""
        self.firstNumber = 0.0
        self.secondNumber = 0.0

    def isValidOperatorInput(self):
        if self.input == "" or self.input == '.' or self.operatorInInput == True:
            return False
        else:
            return True

    def isValidDecimalInput(self):
        if operatorInInput == True:
            if self.input[-1] == '.':
                return False


op = Operation()

def parseInput(input):
    for i in input:
        if i in operators:
            op.operator = i
            numbers = input.split(i)
            op.firstNumber = float(numbers[0])
            op.secondNumber = float(numbers[1])

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def plusButtonPress():
    if op.isValidOperatorInput() == True:
        op.input += "+"
        op.operatorInInput = True
        inpt.configure(text=op.input)
plusButton = tk.Button(root, text='+', command=plusButtonPress)
plusButton.place(x = 125, y = 0)

def equalsButtonPress():
    try:
        op.operatorInInput = False
        parseInput(op.input)
        if op.operator == "+":
            op.input = str(add(op.firstNumber, op.secondNumber))
        elif op.operator == "-":
            op.input = str(subtract(op.firstNumber, op.secondNumber))
        elif op.operator == "*":
            op.input = str(multiply(op.firstNumber, op.secondNumber))
        elif op.operator == "/":
            op.input = str(divide(op.firstNumber, op.secondNumber))
        else:
            op.input = "0"
    except:
        op.input = "error"
    inpt.configure(text=op.input)
equalsButton = tk.Button(root, text='=', command=equalsButtonPress)
equalsButton.place(x = 125, y = 125)

def clearButtonPress():
    op.input = ""
    op.operatorInInput = False
    op.operator = ""
    inpt.configure(text=op.input)
clearButton = tk.Button(root, text='clear', command=clearButtonPress)

frm = tk.Frame(root)

class numberButton:
    def __init__(self, i, j, value):
        self.i = i
        self.j = j
        self.value = value
        self.button = tk.Button(frm, text=value, command=self.numberButtonPress).grid(row=i, column=j)

    def numberButtonPress(self):
        op.input += str(self.value)
        inpt.configure(text=op.input)

value = 1
for i in range(1, 4):
    for j in range(1, 4):
        numberButton(i, j, value)
        value += 1
numberButton(4, 1, 0)
numberButton(4, 3, '.')

frm.pack()
clearButton.pack()
quitButton.place(x=0, y=125)
root.mainloop()