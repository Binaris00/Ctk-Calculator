import customtkinter as ctk

class Convertor_template(ctk.CTk):
   def __init__(self, convertors_dict, convertors_list):
      super().__init__()
      #Basic Calculator Info
      self.title("Calculator")
      self.geometry("500x600")
      self.resizable(False, False)
      
      self.var_input = ""
      self.var_output = ""
      
      self.convertors_dict = convertors_dict
      self.convertors_list = convertors_list
      
      
      ############################
      
      self.text_input = ctk.CTkTextbox(self, width=280, height=70, font=(('Roboto', 30)), corner_radius=1)
      self.text_input.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

      self.text_output = ctk.CTkTextbox(self, width=280, height=70, font=(('Roboto', 30)), corner_radius=1)
      self.text_output.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


      self.menu_selector1 = ctk.CTkOptionMenu(self, width=150, values=self.convertors_list, command=self.output_eval())
      self.menu_selector1.grid(row=0, column=2, columnspan=5, padx=5, pady=5)
      self.menu_selector1.set(self.convertors_list[0])

      self.menu_selector2 = ctk.CTkOptionMenu(self, width=150, values=self.convertors_list, command=self.output_eval())
      self.menu_selector2.grid(row=1, column=2, columnspan=5, padx=5, pady=5)
      self.menu_selector2.set(self.convertors_list[1])
      
      ############################
      
      # First Button Row
      self.button_del_all = ctk.CTkButton(self, text="C", command=lambda: self.delete_last_char(), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_del_all.grid(row=3, column=1, padx=1, pady=1)

      self.button_del = ctk.CTkButton(self, text="CE", command=lambda: self.delete_input_output(), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_del.grid(row=3, column=2, padx=1, pady=1)
      
      
      ####################

      self.button_7 = ctk.CTkButton(self, text="7", command=lambda: self.add_number(7), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_7.grid(row=7, column=0, padx=1, pady=1)

      self.button_8 = ctk.CTkButton(self, text="8", command=lambda: self.add_number(8), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_8.grid(row=7, column=1, padx=1, pady=1)

      self.button_9 = ctk.CTkButton(self, text="9", command=lambda: self.add_number(9), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_9.grid(row=7, column=2, padx=1, pady=1)

      ######################

      self.button_4 = ctk.CTkButton(self, text="4", command=lambda: self.add_number(4), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_4.grid(row=8, column=0, padx=1, pady=1)

      self.button_5 = ctk.CTkButton(self, text="5", command=lambda: self.add_number(5), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_5.grid(row=8, column=1, padx=1, pady=1)

      self.button_6 = ctk.CTkButton(self, text="6", command=lambda: self.add_number(6), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_6.grid(row=8, column=2, padx=1, pady=1)

      #####################

      self.button_1 = ctk.CTkButton(self, text="1", command=lambda: self.add_number(1), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_1.grid(row=9, column=0, padx=1, pady=1)

      self.button_2 = ctk.CTkButton(self, text="2", command=lambda: self.add_number(2), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_2.grid(row=9, column=1, padx=1, pady=1)

      self.button_3 = ctk.CTkButton(self, text="3", command=lambda: self.add_number(3), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_3.grid(row=9, column=2, padx=1, pady=1)
      
      ######################


      self.button_0 = ctk.CTkButton(self, text="0", command=lambda: self.add_number(0), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_0.grid(row=10, column=0, padx=1, pady=1)

      self.button_empty = ctk.CTkButton(self, text="00", command=lambda: self.add_number("00"), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_empty.grid(row=10, column=1, padx=1, pady=1)

      self.button_point = ctk.CTkButton(self, text=".", command=lambda: self.add_number("."), width=160, height=80, font=("Roboto", 22), corner_radius=1)
      self.button_point.grid(row=10, column=2, padx=1, pady=1)


   def add_number(self, number):
      """Add the symbol to operation and output"""
      if number == "." and self.var_input == "":
         return
      
      if number == "." and self.var_input[-1] == ".":
         return
      
      if "." in self.var_input and number == ".":
         return
      
      self.var_input += str(number)
      self.text_input.delete(0.0, "end")
      self.text_input.insert(0.0, self.var_input)
      self.output_eval()
   
   def delete_last_char(self):
      "Well just delete the last character..."
      self.var_input = self.var_input[:-1]
      self.text_input.delete(0.0, "end")
      self.text_input.insert(0.0, self.var_input)
      self.output_eval()

   def delete_input_output(self):
      """Button CE function, only for delete all first_time and second_time"""
      
      self.var_input = ""
      self.text_input.delete(0.0, "end")
      
      self.var_output = ""
      self.text_output.delete(0.0, "end")

   def output_eval(self):
      if self.var_input == "":
         self.var_output = ""
         self.text_output.delete(0.0, "end")
         return
      
      first = self.menu_selector1.get()
      second = self.menu_selector2.get()
      
      if first == second:   
         self.text_output.delete(0.0, "end")
         self.text_output.insert(0.0, self.var_input)
         return

      second_time = eval(f"{self.var_input}{self.convertors_dict[first][second]}")
      
      self.text_output.delete(0.0, "end")
      self.text_output.insert(0.0, second_time)
      
