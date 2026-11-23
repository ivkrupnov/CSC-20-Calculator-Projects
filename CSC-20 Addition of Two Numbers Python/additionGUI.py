# This file builds the desktop calculator window with Tkinter.
# Run from this project folder with: /usr/bin/python3 additionGUI.py

import tkinter as tk
from tkinter import ttk

# Reuse the arithmetic functions from addition.py.
import addition


class AdditionGUI:
    def __init__(self):
        # Create the window and make it close the program when the X is clicked.
        self.frame = tk.Tk()
        self.frame.title("Addition Calculator")

        # Arrange the labels and controls in five rows and two columns.
        for row in range(5):
            self.frame.grid_rowconfigure(row, pad=4)
        self.frame.grid_columnconfigure(0, pad=4)
        self.frame.grid_columnconfigure(1, pad=4)

        # Give each row and column space to fit its controls.
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_rowconfigure(4, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        # Create the labels, number inputs, and operation dropdown.
        tk.Label(self.frame, text="First number").grid(row=0, column=0)
        self.firstNumberField = tk.Entry(self.frame)
        self.firstNumberField.grid(row=0, column=1)
        tk.Label(self.frame, text="Second number").grid(row=1, column=0)
        self.secondNumberField = tk.Entry(self.frame)
        self.secondNumberField.grid(row=1, column=1)
        tk.Label(self.frame, text="Operation").grid(row=2, column=0)
        self.operationBox = ttk.Combobox(
            self.frame,
            values=["Add", "Subtract", "Multiply", "Divide"],
            state="readonly",
        )
        self.operationBox.set("Add")
        self.operationBox.grid(row=2, column=1)

        # Add the calculate button and the area that displays the answer.
        tk.Label(self.frame).grid(row=3, column=0)
        self.calculateButton = tk.Button(
            self.frame, text="Calculate", command=self.calculate
        )
        self.calculateButton.grid(row=3, column=1)
        tk.Label(self.frame, text="Answer").grid(row=4, column=0)
        self.resultLabel = tk.Label(self.frame, text="Result:")
        self.resultLabel.grid(row=4, column=1)

        # Size the window to fit its controls and center it on the screen.
        self.frame.update_idletasks()
        width = self.frame.winfo_width()
        height = self.frame.winfo_height()
        x = (self.frame.winfo_screenwidth() // 2) - (width // 2)
        y = (self.frame.winfo_screenheight() // 2) - (height // 2)
        self.frame.geometry(f"{width}x{height}+{x}+{y}")

    def calculate(self):
        try:
            # Convert the text entered in both fields into integers.
            firstNumber = int(self.firstNumberField.get().strip())
            secondNumber = int(self.secondNumberField.get().strip())
            operation = self.operationBox.get()

            # Call the matching function from addition.py.
            if operation == "Add":
                result = addition.add(firstNumber, secondNumber)
            elif operation == "Subtract":
                result = addition.substract(firstNumber, secondNumber)
            elif operation == "Multiply":
                result = addition.multiply(firstNumber, secondNumber)
            else:
                # Division is not allowed when the second number is zero.
                if secondNumber == 0:
                    self.resultLabel.config(text="Cannot divide by zero")
                    return
                result = addition.divide(firstNumber, secondNumber)

            # Display the calculated answer in the result label.
            self.resultLabel.config(text=str(result))
        except ValueError:
            # This runs when the entered text is not a valid integer.
            self.resultLabel.config(text="Enter valid integers")

    def run(self):
        # Keep the window open and respond to user actions.
        self.frame.mainloop()


# Start the GUI only when this file is run directly.
if __name__ == "__main__":
    AdditionGUI().run()
