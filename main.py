import customtkinter as ctk
import math

# Basic Information for the calculator 
root = ctk.CTk()
root.title("Calculator")
root.geometry("500x600")
root.iconbitmap("resources/icon_calculator.ico")
root.resizable(False, False)
operation = ""

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


conditions = {"": [".", "+", "-", "/", "*"]}

def add_operation(symbol):
   """This function have 3 utilities, can add the symbol to operation, 
   check for not start the operation with operation symbols "+" "-"...
   check for not write "++" "--" in the same operation

   Args:
       symbol (str or ): just the operation to use with eval()
   """
   global operation
   
   
   #Prevent to start with "." "+" "-" "/" "*"
   if operation == "" and symbol in conditions[""]:
      return
   
   #Prevent to put "++" "--" "//"
   elif operation != "":
      if operation[-1] in conditions[""] and symbol in conditions[""]:
         return
   
   if "(" not in operation and symbol == ")":
      return
   
   # Add the symbol to operation and output
   operation += str(symbol)
   output.delete(0.0, "end")
   output.insert(0.0, operation)

def delete_all_operation():
   """Just Delete the operation and output"""
   global operation
   
   operation = ""
   output.delete(0.0, "end")

def delete_last_char():
   global operation
   
   operation = operation[:-1]
   output.delete(0.0, "end")
   output.insert(0.0, operation)

def eval_equal():
   global operation
   if operation == "":
      return
   try:
      operation = str(eval(operation))
   except:
      if "/0" in operation:
         operation = "You cannot divide by zero"
      else:
         operation = "Syntax Error"
      
   output.delete(0.0, "end")
   output.insert(0.0, operation)
   if operation == "Syntax Error":
      operation = ""


def operation_factorial():
   global operation
   if operation == "":
      return
   try:
      operation = str(math.factorial(int(operation)))
   except:
      operation = "Syntax Error"
      
   
   output.delete(0.0, "end")
   output.insert(0.0, operation)
   
def power_two():
   global operation
   if operation == "":
      return
   try:
      operation = str(math.pow(float(eval(operation)), 2))
   except:
      operation = "Syntax Error"
      
   output.delete(0.0, "end")
   output.insert(0.0, operation)
   
def operation_sqrt():
   global operation
   if operation == "":
      return
   try:
      operation = str(math.sqrt(eval(operation)))
   except:
      operation = "Syntax Error"
   
   output.delete(0.0, "end")
   output.insert(0.0, operation)
   

output = ctk.CTkTextbox(root, width=490, height=50, font=(('Roboto', 40)), corner_radius=1)
output.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

"""
------------
(  )  CE C
x²  n!  O  ÷
7  8  9  x
4  5  6  -
1  2  3   +
0  .  O  =
"""


####### First Row 1



button_parenthesis_1 = ctk.CTkButton(root, text="(", command=lambda: add_operation("("), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_parenthesis_1.grid(row=1, column=0, padx=1, pady=1)

button_parenthesis_2 = ctk.CTkButton(root, text=")", command=lambda: add_operation(")"), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_parenthesis_2.grid(row=1, column=1, padx=1, pady=1)

button_del_all = ctk.CTkButton(root, text="C", command=lambda: delete_last_char(), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_del_all.grid(row=1, column=2, padx=1, pady=1)

button_del = ctk.CTkButton(root, text="CE", command=lambda: delete_all_operation(), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_del.grid(row=1, column=3, padx=1, pady=1)



#######



button_empty = ctk.CTkButton(root, text="x²", command=lambda: power_two(), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_empty.grid(row=2, column=0, padx=1, pady=1)

button_empty = ctk.CTkButton(root, text="n!", width=120, command=lambda: operation_factorial(),height=80, font=("Roboto", 22), corner_radius=1)
button_empty.grid(row=2, column=1, padx=1, pady=1)

button_empty = ctk.CTkButton(root, text="√", command=lambda: operation_sqrt(),width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_empty.grid(row=2, column=2, padx=1, pady=1)

button_division = ctk.CTkButton(root, text="÷", command=lambda: add_operation("/"), width=120, height=80,font=("Roboto", 22), corner_radius=1)
button_division.grid(row=2, column=3, padx=1, pady=1)



# BUTTONS NUMBERS



button_7 = ctk.CTkButton(root, text="7", command=lambda: add_operation(7), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_7.grid(row=7, column=0, padx=1, pady=1)

button_8 = ctk.CTkButton(root, text="8", command=lambda: add_operation(8), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_8.grid(row=7, column=1, padx=1, pady=1)

button_9 = ctk.CTkButton(root, text="9", command=lambda: add_operation(9), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_9.grid(row=7, column=2, padx=1, pady=1)

button_multiplication = ctk.CTkButton(root, text="x", command=lambda: add_operation("*"), width=120, height=80,font=("Roboto", 22), corner_radius=1)
button_multiplication.grid(row=7, column=3, padx=1, pady=1)




#######



button_4 = ctk.CTkButton(root, text="4", command=lambda: add_operation(4), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_4.grid(row=8, column=0, padx=1, pady=1)

button_5 = ctk.CTkButton(root, text="5", command=lambda: add_operation(5), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_5.grid(row=8, column=1, padx=1, pady=1)

button_6 = ctk.CTkButton(root, text="6", command=lambda: add_operation(6), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_6.grid(row=8, column=2, padx=1, pady=1)

button_subtraction = ctk.CTkButton(root, text="-", command=lambda: add_operation("-"), width=120, height=80,font=("Roboto", 22), corner_radius=1)
button_subtraction.grid(row=8, column=3, padx=1, pady=1)



#######



button_1 = ctk.CTkButton(root, text="1", command=lambda: add_operation(1), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_1.grid(row=9, column=0, padx=1, pady=1)

button_2 = ctk.CTkButton(root, text="2", command=lambda: add_operation(2), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_2.grid(row=9, column=1, padx=1, pady=1)

button_3 = ctk.CTkButton(root, text="3", command=lambda: add_operation(3), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_3.grid(row=9, column=2, padx=1, pady=1)

button_addition = ctk.CTkButton(root, text="+", command=lambda: add_operation("+"), width=120, height=80,font=("Roboto", 22), corner_radius=1)
button_addition.grid(row=9, column=3, padx=1, pady=1)



####
#Ultimate row
button_0 = ctk.CTkButton(root, text="0", command=lambda: add_operation(0), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_0.grid(row=10, column=0, padx=1, pady=1)

button_empty = ctk.CTkButton(root, text="00", command=lambda: add_operation("00"), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_empty.grid(row=10, column=1, padx=1, pady=1)

button_point = ctk.CTkButton(root, text=".", command=lambda: add_operation("."), width=120, height=80, font=("Roboto", 22), corner_radius=1)
button_point.grid(row=10, column=2, padx=1, pady=1)

button_equal = ctk.CTkButton(root, text="=", command=lambda: eval_equal(), width=120, height=80 ,font=("Roboto", 22), corner_radius=1)
button_equal.grid(row=10, column=3, padx=1, pady=1)



##########
root.mainloop()