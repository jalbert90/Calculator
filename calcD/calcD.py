import tkinter as tk

#Create a Calculator class that extends tk.Frame
class Calculator(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):        
        #Create an Entry widget to display the current expression
        self.display = tk.Entry(self.master, width=30, borderwidth=5)

        #Create a text variable to keep track of the current expression
        self.text = ""
        
        #Add the display to the top of the root window
        self.display.grid(row=0, column=0, columnspan=3, padx=10 , pady=10)

        #Create a list of button labels
        button_labels = ["7","8","9","/","4","5","6","*","1","2","3","-",".","0","C","+", "="]
        #Create a dictionary to store the buttons
        self.buttons = {}
        #use the grid layout to place the buttons in table 
        #by iterating over the list and then after every fourth item it will increament the row count
        r=1
        c=0
        for label in button_labels:
            if label == "C":
                self.buttons[label] = tk.Button(self.master, text = label, padx = 39, pady = 20, command = self.clear)
            elif label == "=":
                self.buttons[label] = tk.Button(self.master, text = label, padx = 91, pady = 20, command = self.calculate)
            else: 
                self.buttons[label] = tk.Button(self.master, text = label, padx = 40, pady = 20, command = lambda l=label :self.button_click(l))
            self.buttons[label].grid(row = r, column = c) 
            c += 1 
            if c>3 : 
                c=0 
                r+=1
    
    #displays the pressed button character in the input field 
    def button_click(self , number):
        self.text=self.display.get()+number 
        self.display.delete(0,"end")
        self.display.insert(0,self.text)
    # clears the input field     
    def clear (self): 
        self.display.delete(0,"end")
    # calculates the inputed expression    
    def calculate (self):
        self.text = eval(self.display.get())
        self.display.delete(0, "end")
        self.display.insert(0, self.text)



root = tk.Tk()
app = Calculator(root)
app.mainloop()