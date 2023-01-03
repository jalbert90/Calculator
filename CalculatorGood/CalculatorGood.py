import tkinter as tk

root = tk.Tk()
root.title('calc')
root.geometry("160x150")
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

class Input:
    def __init__(self):
        self.expression = ""
        self.input1 = ""
        self.input2 = ""
        self.operatorInInput = False
        self.operator = ""
        self.firstNumber = 0.0
        self.secondNumber = 0.0
        self.result = 0.0
        self.firstNumberInInput = False

    def reset(self):
        self.expression = ""
        self.input1 = ""
        self.input2 = ""
        self.operatorInInput = False
        self.operator = ""
        self.firstNumber = 0.0
        self.secondNumber = 0.0
        self.result = 0.0
        self.firstNumberInInput = False

    def isValidOperatorInput(self):
        if self.expression == "" or self.expression == '.' or self.operatorInInput == True:
            return False
        else:
            return True

    def isValidDecimalInput(self, input):
        for i in input:
            if i == '.':
                return False
        return True

    def setOperator(self, operator):
        self.operator = operator
        self.expression += operator
        self.operatorInInput = True
        self.firstNumberInInput = True
        inpt.configure(text=self.expression)

ip = Input()

def convertInputsToFloats(input1, input2):
    try:
        ip.firstNumber = float(input1)
        if input2 != "":
            ip.secondNumber = float(input2)
    except:
        print("Couldn't convert inputs to floats")

def plusButtonPress():
    if ip.isValidOperatorInput() == True:
        ip.setOperator('+')
plusButton = tk.Button(root, text='+', command=plusButtonPress)
plusButton.place(x=140, y=25)

def subtractButtonPress():
    if ip.isValidOperatorInput() == True:
        ip.setOperator('-')
subtractButton = tk.Button(root, text='-', command=subtractButtonPress)
subtractButton.place(x=140, y=50)

def multiplyButtonPress():
    if ip.isValidOperatorInput() == True:
        ip.setOperator('*')
multiplyButton = tk.Button(root, text='*', command=multiplyButtonPress)
multiplyButton.place(x=140, y=75)

def divideButtonPress():
    if ip.isValidOperatorInput() == True:
        ip.setOperator('/')
divideButton = tk.Button(root, text='/', command=divideButtonPress)
divideButton.place(x=140, y=100)

def equalsButtonPress():
    try:
        ip.operatorInInput = False
        if ip.expression != "":
            convertInputsToFloats(ip.input1, ip.input2)
            ip.result = operation(ip.operator, ip.firstNumber, ip.secondNumber)
            ip.expression = str(ip.result)
        ip.input1 = ip.expression
        ip.input2 = ""
    except:
        ip.reset()
        ip.expression = "error"
        print("Error in equalsButtonPress()")
    inpt.configure(text=ip.expression)
equalsButton = tk.Button(root, text='=', command=equalsButtonPress)
equalsButton.place(x = 140, y = 125)

def clearButtonPress():
    ip.reset()
    inpt.configure(text=ip.expression)
clearButton = tk.Button(root, text='clear', command=clearButtonPress)

frm = tk.Frame(root)

class numberButton:
    def __init__(self, i, j, value):
        self.i = i
        self.j = j
        self.value = value
        self.button = tk.Button(frm, text=value, command=self.numberButtonPress).grid(row=i, column=j)

    def numberButtonPress(self):
        if ip.firstNumberInInput == False:
            ip.input1 += str(self.value)
        else:
            ip.input2 += str(self.value)
        ip.expression += str(self.value)
        inpt.configure(text=ip.expression)

value = 1
for i in range(1, 4):
    for j in range(1, 4):
        numberButton(i, j, value)
        value += 1
numberButton(4, 1, 0)

def decimalButtonPress():
    if ip.firstNumberInInput == False and ip.isValidDecimalInput(ip.input1):
        ip.input1 += str('.')
        ip.expression += str('.')
        inpt.configure(text=ip.expression)
    if ip.firstNumberInInput == True and ip.isValidDecimalInput(ip.input2):
        ip.input2 += str('.')
        ip.expression += str('.')
        inpt.configure(text=ip.expression)
decimalButton = tk.Button(root, text='.', command=decimalButtonPress)
decimalButton.place(x=90, y=99)

frm.pack()
clearButton.pack()
quitButton.place(x=0, y=125)
root.mainloop()