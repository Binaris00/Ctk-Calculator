import customtkinter as ctk

#Basic Calculator Info
root = ctk.CTk()
root.title("Calculator")
root.geometry("500x600")
root.resizable(False, False)

first_time = ""
second_time = ""
convertors = {
   "Bytes": {"Kilobytes":"/1024", "Megabytes":"/1048576", "Gigabytes":"/1073741824", "Terabytes":"/1099511627776", "Petabytes":"/1125899906842624"},
   "Kilobytes": {"Bytes":"*1024", "Megabytes":"/1024", "Gigabytes":"/1048576", "Terabytes":"/1073741824", "Petabytes":"/1099511627776"},
   "Megabytes": {"Bytes":"*1048576", "Kilobytes":"*1024", "Gigabytes":"/1024", "Terabytes":"/1048576", "Petabytes":"/1073741824"},
   "Gigabytes": {"Bytes":"*1073741824", "Kilobytes":"*1048576", "Megabytes":"*1024", "Terabytes":"/1024", "Petabytes":"/1048576"},
   "Terabytes": {"Bytes":"*1099511627776", "Kilobytes":"*1073741824", "Megabytes":"*1048576", "Gigabytes":"*1024", "Petabytes":"/1024"},
   "Petabytes": {"Bytes":"*1125899906842624", "Kilobytes":"*1099511627776", "Megabytes":"*1073741824", "Gigabytes":"*1048576", "Terabytes":"*1024"},
}


def add_number(number):
   global first_time
      
   # Add the symbol to operation and output
   first_time += str(number)
   time_input.delete(0.0, "end")
   time_input.insert(0.0, first_time)
   time_eval()

def delete_last_char():
   global first_time
   
   first_time = first_time[:-1]
   time_input.delete(0.0, "end")
   time_input.insert(0.0, first_time)
   time_eval()




def delete_input_output():
   """Button CE function, only for delete all first_time and second_time"""
   global first_time
   
   first_time = ""
   time_input.delete(0.0, "end")
   
   second_time = ""
   time_output.delete(0.0, "end")

def time_eval():
   global first_time
   
   if first_time == "":
      second_time = ""
      time_output.delete(0.0, "end")
      return
   
   first = time_selector1.get()
   second = time_selector2.get()
   
   if first == second:   
      time_output.delete(0.0, "end")
      time_output.insert(0.0, first_time)
      return

   second_time = eval(f"{first_time}{convertors[first][second]}")
   
   time_output.delete(0.0, "end")
   time_output.insert(0.0, second_time)
   
   
time_input = ctk.CTkTextbox(root, width=250, height=70, font=(('Roboto', 40)), corner_radius=1)
time_input.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

time_output = ctk.CTkTextbox(root, width=250, height=70, font=(('Roboto', 40)), corner_radius=1)
time_output.grid(row=1, column=0, columnspan=2, padx=5, pady=5)




time_selector1 = ctk.CTkOptionMenu(root, width=150, values=["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"], command=time_eval())
time_selector1.grid(row=0, column=2, columnspan=5, padx=5, pady=5)
time_selector1.set("Gigabytes")

time_selector2 = ctk.CTkOptionMenu(root, width=150, values=["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"], command=time_eval())
time_selector2.grid(row=1, column=2, columnspan=5, padx=5, pady=5)
time_selector2.set("Megabytes")



# First Button Row

button_del_all = ctk.CTkButton(root, text="C", command=lambda: delete_last_char(), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_del_all.grid(row=3, column=1, padx=1, pady=1)

button_del = ctk.CTkButton(root, text="CE", command=lambda: delete_input_output(), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_del.grid(row=3, column=2, padx=1, pady=1)

####################

button_7 = ctk.CTkButton(root, text="7", command=lambda: add_number(7), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_7.grid(row=7, column=0, padx=1, pady=1)

button_8 = ctk.CTkButton(root, text="8", command=lambda: add_number(8), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_8.grid(row=7, column=1, padx=1, pady=1)

button_9 = ctk.CTkButton(root, text="9", command=lambda: add_number(9), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_9.grid(row=7, column=2, padx=1, pady=1)

######################


button_4 = ctk.CTkButton(root, text="4", command=lambda: add_number(4), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_4.grid(row=8, column=0, padx=1, pady=1)

button_5 = ctk.CTkButton(root, text="5", command=lambda: add_number(5), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_5.grid(row=8, column=1, padx=1, pady=1)

button_6 = ctk.CTkButton(root, text="6", command=lambda: add_number(6), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_6.grid(row=8, column=2, padx=1, pady=1)

#####################

button_1 = ctk.CTkButton(root, text="1", command=lambda: add_number(1), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_1.grid(row=9, column=0, padx=1, pady=1)

button_2 = ctk.CTkButton(root, text="2", command=lambda: add_number(2), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_2.grid(row=9, column=1, padx=1, pady=1)

button_3 = ctk.CTkButton(root, text="3", command=lambda: add_number(3), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_3.grid(row=9, column=2, padx=1, pady=1)

######################


button_0 = ctk.CTkButton(root, text="0", command=lambda: add_number(0), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_0.grid(row=10, column=0, padx=1, pady=1)

button_empty = ctk.CTkButton(root, text="00", command=lambda: add_number("00"), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_empty.grid(row=10, column=1, padx=1, pady=1)

button_point = ctk.CTkButton(root, text=".", command=lambda: add_number("."), width=160, height=80, font=("Roboto", 22), corner_radius=1)
button_point.grid(row=10, column=2, padx=1, pady=1)




root.mainloop()