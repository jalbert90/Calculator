import tkinter as tk

root = tk.Tk()
root.title('calc')
root.geometry("150x150")
root.resizable(False, False)

inpt = tk.Label(root, text="")
inpt.pack()
quitButton = tk.Button(root, text='quit', command=root.destroy)

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    try:
        return a / b
    except:
        print("error in divide(a, b)--possible division by 0")

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

    def setOperator(self, operator):
        self.operator = operator
        self.input += operator
        self.operatorInInput = True
        self.firstNumberInInput = True
        inpt.configure(text=self.input)

op = Operation()

def convertInputsToFloats(input1, input2):
    try:
        op.firstNumber = float(input1)
        if input2 != "":
            op.secondNumber = float(input2)
    except:
        print("Couldn't convert inputs to floats")

def plusButtonPress():
    if op.isValidOperatorInput() == True:
        op.setOperator('+')
plusButton = tk.Button(root, text='+', command=plusButtonPress)
plusButton.place(x=125, y=0)

def subtractButtonPress():
    if op.isValidOperatorInput() == True:
        op.setOperator('-')
subtractButton = tk.Button(root, text='-', command=subtractButtonPress)
subtractButton.place(x=125, y=25)

def multiplyButtonPress():
    if op.isValidOperatorInput() == True:
        op.setOperator('*')
multiplyButton = tk.Button(root, text='*', command=multiplyButtonPress)
multiplyButton.place(x=125, y=50)

def divideButtonPress():
    if op.isValidOperatorInput() == True:
        op.setOperator('/')
divideButton = tk.Button(root, text='/', command=divideButtonPress)
divideButton.place(x=125, y=75)

def equalsButtonPress():
    try:
        op.operatorInInput = False
        if op.input != "":
            convertInputsToFloats(op.input1, op.input2)
            op.result = operation(op.operator, op.firstNumber, op.secondNumber)
            op.output = str(op.result)
        op.input1 = op.output
        op.input2 = ""
        op.input = op.output
    except:
        op.output = "error"
        op.input1 = "0"
        op.input2 = "0"
        op.firstNumber = 0.0
        op.secondNumber = 0.0
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
    op.firstNumber = 0.0
    op.secondNumber = 0.0
    op.operatorInInput = False
    op.firstNumberInInput = False
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