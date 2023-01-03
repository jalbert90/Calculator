import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # creating entry widget to display the current equation
        self.equation = tk.Entry(master, width=36, borderwidth=5)

        #  create button widgets for each number and each operator
        button_1 = tk.Button(master, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        button_2 = tk.Button(master, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        button_3 = tk.Button(master, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        button_4 = tk.Button(master, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        button_5 = tk.Button(master, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        button_6 = tk.Button(master, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        button_7 = tk.Button(master, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        button_8 = tk.Button(master, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        button_9 = tk.Button(master, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        button_0 = tk.Button(master, text="0", padx=40, pady=20, command=lambda: self.button_click(0))
        button_add = tk.Button(master, text="+", padx=39, pady=20, command=lambda: self.button_click("+"))
        button_subtract = tk.Button(master, text="-", padx=41, pady=20, command=lambda: self.button_click("-"))
        button_multiply = tk.Button(master, text="*", padx=40, pady=20, command=lambda: self.button_click("*"))
        button_divide = tk.Button(master, text="/", padx=41, pady=20, command=lambda: self.button_click("/"))
        button_equal = tk.Button(master, text="=", padx=9, pady=20, command=lambda: self.button_click("="))



root = tk.Tk()
app = Calculator(root)
root.mainloop()