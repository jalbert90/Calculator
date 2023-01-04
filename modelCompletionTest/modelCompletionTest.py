import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.master.minsize(width=200, height=30)

    def create_widgets(self):
        # entry widget to display current equation
        self.current = tk.StringVar()
        self.current.set("")
        self.entry = tk.Entry(self, textvariable=self.current)
        self.entry.pack(side="top")

        # frame to hold buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side="bottom")

        # number buttons
        for i in range(1, 10):
            button = tk.Button(self.button_frame, text=str(i), command=lambda val=i: self.append_val(val))
            button.grid(row=(9-i)//3, column=(i-1)%3)

        # button for zero
        button = tk.Button(self.button_frame, text="0", command=lambda: self.append_val(0))
        button.grid(row=3, column=0)

        # clear button
        button = tk.Button(self.button_frame, text="C", command=lambda: self.clear())
        button.grid(row=3, column=1)

        # equal button
        button = tk.Button(self.button_frame, text="=", command=lambda: self.calculate())
        button.grid(row=3, column=2)

        # operator buttons
        button = tk.Button(self.button_frame, text="+", command=lambda: self.append_operator("+"))
        button.grid(row=0, column=3)
        button = tk.Button(self.button_frame, text="-", command=lambda: self.append_operator("-"))
        button.grid(row=1, column=3)
        button = tk.Button(self.button_frame, text="*", command=lambda: self.append_operator("*"))
        button.grid(row=2, column=3)
        button = tk.Button(self.button_frame, text="/", command=lambda: self.append_operator("/"))
        button.grid(row=3, column=3)

    def append_val(self, val):
        self.current.set(self.current.get() + str(val))

    def clear(self):
        self.current.set("")

    def append_operator(self, operator):
        if len(self.current.get()) == 0:
            return
        if self.current.get()[-1] in ["+", "-", "*", "/"]:
            self.current.set(self.current.get()[:-1]) # remove last operator
        self.current.set(self.current.get() + operator)
        
    def calculate(self):
        try:
            self.current.set(eval(self.current.get())) # calculate the result of the equation
        except:
            self.current.set('Error') # catch any evaluation error
    
root = tk.Tk()
calc = Calculator(master=root)
calc.mainloop()