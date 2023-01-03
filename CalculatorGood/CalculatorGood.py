import tkinter as tk

root = tk.Tk()
root.title('calc')
root.geometry("150x150")
root.resizable(False, False)

inpt = tk.Label(root, text="")
inpt.pack()
quitButton = tk.Button(root, text='quit', command=root.destroy)

#OPERATORS = {"+", "-", "*", "/"}

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

OPERATIONS = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide}

def operation(operator, a, b):
    return OPERATIONS[operator](a, b)

class Operation:
    def __init__(self):
        self.input = ""
        self.input1 = ""
        self.input2 = ""
        self.operatorInInput = False
        self.operator = ""
        self.firstNumber = 0.0
        self.secondNumber = 0.0
        self.result = 0.0
        self.output = ""
        self.firstNumberInInput = False

    def isValidOperatorInput(self):
        if self.input == "" or self.input == '.' or self.operatorInInput == True:
            return False
        else:
            return True

op = Operation()

def parseInput(input):
    for i in input:
        if i in OPERATORS:
            op.operator = i
            numbers = input.split(i)
            op.firstNumber = float(numbers[0])
            op.secondNumber = float(numbers[1])

def convertInputsToFloats(input1, input2):
    try:
        op.firstNumber = float(input1)
        op.secondNumber = float(input2)
    except:
        print("Couldn't convert inputs to floats")

def plusButtonPress():
    if op.isValidOperatorInput() == True:
        op.operator = '+'
        op.input += "+"
        op.operatorInInput = True
        op.firstNumberInInput = True
        inpt.configure(text=op.input)
plusButton = tk.Button(root, text='+', command=plusButtonPress)
plusButton.place(x=125, y=0)

def subtractButtonPress():
    if op.isValidOperatorInput() == True:
        op.input += "-"
        op.operatorInInput = True
        inpt.configure(text=op.input)
subtractButton = tk.Button(root, text='-', command=subtractButtonPress)
subtractButton.place(x=125, y=25)

def equalsButtonPress():
    try:
        op.operatorInInput = False
        convertInputsToFloats(op.input1, op.input2)
        op.result = operation(op.operator, op.firstNumber, op.secondNumber)
        op.output = str(op.result)
        op.input1 = op.output
        op.input2 = ""
        op.input = op.output
    except:
        op.output = "0"
        op.input1 = "0"
        op.input = "0"
        op.operatorInInput = False
        print("Error in equalsButtonPress()")
    inpt.configure(text=op.output)
equalsButton = tk.Button(root, text='=', command=equalsButtonPress)
equalsButton.place(x = 125, y = 125)

def clearButtonPress():
    op.input = ""
    op.input1 = ""
    op.input2 = ""
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
        if op.firstNumberInInput == False:
            op.input1 += str(self.value)
        else:
            op.input2 += str(self.value)
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