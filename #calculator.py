#calculator 
import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.result_var = tk.StringVar()
        self.create_widgets()
        
    def create_widgets(self):
        result_frame = tk.Frame(self)
        result_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")
        
        result_entry = tk.Entry(result_frame, textvariable=self.result_var, font=("Arial", 18), bd=5, state='disabled', justify='left')
        result_entry.pack(fill='both', expand=True)
    
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('AC', 0, 3),  # All Clear button
        ]
        
        for (text, row, col) in buttons:
            if text == 'AC':
                button = tk.Button(self, text=text, font=("Arial", 14), command=self.clear_display, bd=3)
            else:
                button = tk.Button(self, text=text, font=("Arial", 14), command=lambda t=text: self.on_button_click(t), bd=3)
            button.grid(row=row, column=col, sticky="nsew")

        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        
    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(self.result_var.get() + char)

    def clear_display(self):
        self.result_var.set("")

if __name__== "__main__":
    app = CalculatorApp()
    app.mainloop()