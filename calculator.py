import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # Create Entry widget to display the result
        self.result = tk.Entry(master, width=20, font=('Arial', 16), justify='right', bg='black', fg='white')
        self.result.grid(row=0, column=0, columnspan=5)

        # Create buttons for basic operations
        self.create_button('sin(', 1, 0, 'black')
        self.create_button('cos(', 1, 1, 'black')
        self.create_button('tan(', 1, 2, 'black')
        self.create_button('^', 1, 3, 'black')
        self.create_button('(', 1, 4, 'black')

        self.create_button('asin(', 2, 0, 'black')
        self.create_button('acos(', 2, 1, 'black')
        self.create_button('atan(', 2, 2, 'black')
        self.create_button('sqrt', 2, 3, 'black')
        self.create_button(')', 2, 4, 'black')

        self.create_button('log', 3, 0, 'black')
        self.create_button('ln', 3, 1, 'black')
        self.create_button('pi', 3, 2, 'black')
        self.create_button('e', 3, 3, 'black')
        self.create_button('C', 3, 4, 'red')

        # Create buttons for digits and basic operators
        self.create_button('7', 4, 0, 'black')
        self.create_button('8', 4, 1, 'black')
        self.create_button('9', 4, 2, 'black')
        self.create_button('/', 4, 3, 'black')
        self.create_button('*', 4, 4, 'black')

        self.create_button('4', 5, 0, 'black')
        self.create_button('5', 5, 1, 'black')
        self.create_button('6', 5, 2, 'black')
        self.create_button('-', 5, 3, 'black')
        self.create_button('+', 5, 4, 'black')

        self.create_button('1', 6, 0, 'black')
        self.create_button('2', 6, 1, 'black')
        self.create_button('3', 6, 2, 'black')
        self.create_button('.', 6, 3, 'black')
        self.create_button('=', 6, 4, 'black')

        self.create_button('0', 7, 0, 'black')
        self.create_button('(', 7, 1, 'black')
        self.create_button(')', 7, 2, 'black')
        self.create_button('⌫', 7, 3, 'black')

    def create_button(self, text, row, column, color):
        if text == '⌫':
            button = tk.Button(self.master, text=text, width=4, height=2, font=('Arial', 16), bg=color, fg='white', command=self.remove)
        else:
            button = tk.Button(self.master, text=text, width=4, height=2, font=('Arial', 16), bg=color, fg='white', command=lambda:self.click(text))
        button.grid(row=row, column=column)

    def click(self, key):
        if key == '=':
            # Calculate theresult
            try:
                expression = self.result.get()
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')
                expression = expression.replace('asin', 'math.asin')
                expression = expression.replace('acos', 'math.acos')
                expression = expression.replace('atan', 'math.atan')
                expression = expression.replace('sqrt', 'math.sqrt')
                expression = expression.replace('log', 'math.log10')
                expression = expression.replace('ln', 'math.log')
                expression = expression.replace('pi', 'math.pi')
                expression = expression.replace('e', 'math.e')
                result = eval(expression)
            except:
                result = 'Error'
            self.result.delete(0, 'end')
            self.result.insert('end', result)
        elif key == 'C':
            # Clear the result
            self.result.delete(0, 'end')
        elif key == '⌫':
            # Remove the last character
            self.remove()
        else:
            # Add the key to the result
            self.result.insert('end', key)

    def remove(self):
        # Remove the last character from the result
        current_text = self.result.get()
        self.result.delete(0, 'end')
        self.result.insert(0, current_text[:-1])

root = tk.Tk()
root.configure(bg='black')
calculator = Calculator(root)
root.mainloop()
