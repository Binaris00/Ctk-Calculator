import customtkinter as ctk
import math

import customtkinter as ctk
import math

class Calculator(ctk.CTk):
   def __init__(self):
      super().__init__()
      self.title("Calculator")
      self.geometry("500x600")
      self.iconbitmap("resources/icon_calculator.ico")
      self.resizable(False, False)
      
      self.operation = ""
      self.conditions = {"": [".", "+", "-", "/", "*"]}
      
      self.output = ctk.CTkTextbox(self, width=490, height=50, font=(('Roboto', 40)), corner_radius=1)
      self.output.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
         

      ####### First Row 1



      self.button_parenthesis_1 = ctk.CTkButton(self, text="(", command=lambda: self.add_operation("("), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_parenthesis_1.grid(row=1, column=0, padx=1, pady=1)

      self.button_parenthesis_2 = ctk.CTkButton(self, text=")", command=lambda: self.add_operation(")"), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_parenthesis_2.grid(row=1, column=1, padx=1, pady=1)

      self.button_del_all = ctk.CTkButton(self, text="C", command=lambda: self.delete_last_char(), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_del_all.grid(row=1, column=2, padx=1, pady=1)

      self.button_del = ctk.CTkButton(self, text="CE", command=lambda: self.delete_all_operation(), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_del.grid(row=1, column=3, padx=1, pady=1)



      #######



      self.button_empty = ctk.CTkButton(self, text="x²", command=lambda: self.power_two(), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_empty.grid(row=2, column=0, padx=1, pady=1)

      self.button_empty = ctk.CTkButton(self, text="n!", width=120, command=lambda: self.operation_factorial(),height=80, font=("Roboto", 22), corner_radius=1)
      self.button_empty.grid(row=2, column=1, padx=1, pady=1)

      self.button_empty = ctk.CTkButton(self, text="√", command=lambda: self.operation_sqrt(),width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_empty.grid(row=2, column=2, padx=1, pady=1)

      self.button_division = ctk.CTkButton(self, text="÷", command=lambda: self.add_operation("/"), width=120, height=80,font=("Roboto", 22), corner_radius=1)
      self.button_division.grid(row=2, column=3, padx=1, pady=1)



      # BUTTONS NUMBERS



      self.button_7 = ctk.CTkButton(self, text="7", command=lambda: self.add_operation(7), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_7.grid(row=7, column=0, padx=1, pady=1)

      self.button_8 = ctk.CTkButton(self, text="8", command=lambda: self.add_operation(8), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_8.grid(row=7, column=1, padx=1, pady=1)

      self.button_9 = ctk.CTkButton(self, text="9", command=lambda: self.add_operation(9), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_9.grid(row=7, column=2, padx=1, pady=1)

      self.button_multiplication = ctk.CTkButton(self, text="x", command=lambda: self.add_operation("*"), width=120, height=80,font=("Roboto", 22), corner_radius=1)
      self.button_multiplication.grid(row=7, column=3, padx=1, pady=1)




      #######



      self.button_4 = ctk.CTkButton(self, text="4", command=lambda: self.add_operation(4), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_4.grid(row=8, column=0, padx=1, pady=1)

      self.button_5 = ctk.CTkButton(self, text="5", command=lambda: self.add_operation(5), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_5.grid(row=8, column=1, padx=1, pady=1)

      self.button_6 = ctk.CTkButton(self, text="6", command=lambda: self.add_operation(6), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_6.grid(row=8, column=2, padx=1, pady=1)

      self.button_subtraction = ctk.CTkButton(self, text="-", command=lambda: self.add_operation("-"), width=120, height=80,font=("Roboto", 22), corner_radius=1)
      self.button_subtraction.grid(row=8, column=3, padx=1, pady=1)



      #######



      self.button_1 = ctk.CTkButton(self, text="1", command=lambda: self.add_operation(1), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_1.grid(row=9, column=0, padx=1, pady=1)

      self.button_2 = ctk.CTkButton(self, text="2", command=lambda: self.add_operation(2), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_2.grid(row=9, column=1, padx=1, pady=1)

      self.button_3 = ctk.CTkButton(self, text="3", command=lambda: self.add_operation(3), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_3.grid(row=9, column=2, padx=1, pady=1)

      self.button_addition = ctk.CTkButton(self, text="+", command=lambda: self.add_operation("+"), width=120, height=80,font=("Roboto", 22), corner_radius=1)
      self.button_addition.grid(row=9, column=3, padx=1, pady=1)



      ####
      #Ultimate row
      self.button_0 = ctk.CTkButton(self, text="0", command=lambda: self.add_operation(0), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_0.grid(row=10, column=0, padx=1, pady=1)

      self.button_empty = ctk.CTkButton(self, text="00", command=lambda: self.add_operation("00"), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_empty.grid(row=10, column=1, padx=1, pady=1)

      self.button_point = ctk.CTkButton(self, text=".", command=lambda: self.add_operation("."), width=120, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_point.grid(row=10, column=2, padx=1, pady=1)

      self.button_equal = ctk.CTkButton(self, text="=", command=lambda: self.eval_equal(), width=120, height=80 ,font=("Roboto", 22), corner_radius=1)
      self.button_equal.grid(row=10, column=3, padx=1, pady=1)



   ##########
      
   def add_operation(self, symbol):
      """This function have 3 utilities, can add the symbol to operation, 
      check for not start the operation with operation symbols "+" "-"...
      check for not write "++" "--" in the same operation

      Args:
         symbol (str or ): just the operation to use with eval()
      """
      #Prevent to start with "." "+" "-" "/" "*"
      if self.operation == "" and symbol in self.conditions[""]:
         return
      
      #Prevent to put "++" "--" "//"
      elif self.operation != "":
         if self.operation[-1] in self.conditions[""] and symbol in self.conditions[""]:
            return
      
      if "(" not in self.operation and symbol == ")":
         return
      
      # Add the symbol to operation and output
      self.operation += str(symbol)
      self.output.delete(0.0, "end")
      self.output.insert(0.0, self.operation)

   def delete_all_operation(self):
      """Just Delete the operation and output"""
   
      self.operation = ""
      self.output.delete(0.0, "end")


   def delete_last_char(self):
      
      self.operation = self.operation[:-1]
      self.output.delete(0.0, "end")
      self.output.insert(0.0, self.operation)

   def eval_equal(self):
      
      if self.operation == "":
         return
      try:
         self.operation = str(eval(self.operation))
      except:
         if "/0" in self.operation:
            self.operation = "You cannot divide by zero"
         else:
            self.operation = "Syntax Error"
         
      self.output.delete(0.0, "end")
      self.output.insert(0.0, self.operation)
      if self.operation == "Syntax Error":
         self.operation = ""

   def operation_factorial(self):
      
      if self.operation == "":
         return
      try:
         self.operation = str(math.factorial(int(self.operation)))
      except:
         self.operation = "Syntax Error"
         
      
      self.output.delete(0.0, "end")
      self.output.insert(0.0, self.operation)

   def power_two(self):
      if self.operation == "":
         return
      try:
         self.operation = str(math.pow(float(eval(self.operation)), 2))
      except:
         self.operation = "Syntax Error"
         
      self.output.delete(0.0, "end")
      self.output.insert(0.0, self.operation)
   
   def operation_sqrt(self):

      if self.operation == "":
         return
      try:
         self.operation = str(math.sqrt(eval(self.operation)))
      except:
         self.operation = "Syntax Error"
      
      self.output.delete(0.0, "end")
      self.output.insert(0.0, self.operation)
      
      
   """
   ------------
   (  )  CE C
   x²  n!  O  ÷
   7  8  9  x
   4  5  6  -
   1  2  3   +
   0  .  O  =
   """
   
   

calculator = Calculator()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
calculator.mainloop()