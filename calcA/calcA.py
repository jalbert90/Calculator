import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        
        # Entry box
        self.result = tk.Entry(self.master, width=20, font=('Arial', 16))
        self.result.grid(row=0, column=0, columnspan=4)
        
        # Buttons
        self.create_button("1", 1, 1)
        self.create_button("2", 1, 2)
        self.create_button("3", 1, 3)
        self.create_button("4", 2, 1)
        self.create_button("5", 2, 2)
        self.create_button("6", 2, 3)
        self.create_button("7", 3, 1)
        self.create_button("8", 3, 2)
        self.create_button("9", 3, 3)
        self.create_button("0", 4, 2)
        self.create_button("+", 1, 4)
        self.create_button("-", 2, 4)
        self.create_button("*", 3, 4)
        self.create_button("/", 4, 4)
        self.create_button("C", 4, 1)
        self.create_button(".", 4, 3)
        self.create_button("=", 5, 4)
        
    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16), command=lambda: self.button_click(text))
        button.grid(row=row, column=column)
        
    def button_click(self, text):
        if text == "C":
            self.result.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.result.get())
                self.result.delete(0, tk.END)
                self.result.insert(0, result)
            except:
                self.result.delete(0, tk.END)
                self.result.insert(0, "Error")
        else:
            self.result.insert(tk.END, text)
            

root = tk.Tk()
calc = Calculator(root)
root.mainloop()