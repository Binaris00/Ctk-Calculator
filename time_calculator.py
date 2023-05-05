import customtkinter as ctk

#Basic Calculator Info
root = ctk.CTk()
root.title("Calculator")
root.geometry("500x600")
root.resizable(False, False)

first_time = ""
second_time = ""
convertors = {
   "Microseconds": {"Milliseconds":"/1000", "Seconds":"/1000000", "Minutes":"*0.000016666666666666668", "Hours":"*0.0000002777777777777778", "Days":"*0.000000011574074074074074", "Weeks":"*0.0000000016534391534391535", "Years":"*0.00000000003168876416355726"},
   "Milliseconds": {"Microseconds":"*1000", "Seconds":"/1000", "Minutes":"*0.000016666666666666668", "Hours":"*0.0000002777777777777778", "Days":"*0.000000011574074074074074", "Weeks":"*0.0000000016534391534391535", "Years":"*0.00000000003168876416355726"},
   "Seconds": {"Microseconds":"*1000000", "Milliseconds":"*1000", "Minutes":"/60", "Hours":"*0.0002777777777777778", "Days":"*0.000011574074074074074", "Weeks":"*0.0000016534391534391535", "Years":"*0.00000003168876416355726"},
   "Minutes": {"Microseconds":"*60000000", "Milliseconds":"*60000", "Seconds":"*60", "Hours":"/60", "Days":"*0.041666666666666664", "Weeks":"*0.005952380952380952", "Years":"*0.00011415525114155251"},
   "Hours": {"Microseconds":"*3600000000", "Milliseconds":"*3600000", "Seconds":"*3600", "Minutes":"*60", "Days":"/24", "Weeks":"*0.14285714285714285", "Years":"*0.0027397260273972603"},
   "Days": {"Microseconds":"*86400000000", "Milliseconds":"*86400000", "Seconds":"*86400", "Minutes":"*1440", "Hours":"*24", "Weeks":"/7", "Years":"*0.0027397260273972603"},
   "Months": {"Microseconds":"*2628000000000", "Milliseconds":"*2628000000", "Seconds":"*2628000", "Minutes":"*43800", "Hours":"*730", "Days":"*30", "Weeks":"*4.345238095238095", "Years":"*0.08333333333333333"},
   "Weeks": {"Microseconds":"*604800000000", "Milliseconds":"*604800000", "Seconds":"*604800", "Minutes":"*10080", "Hours":"*168", "Days":"*7", "Years":"*0.05214285714285714"},
   "Years": {"Microseconds":"*31536000000000", "Milliseconds":"*31536000000", "Seconds":"*31536000", "Minutes":"*525600", "Hours":"*8760", "Days":"*365", "Weeks":"*52.14285714285714"}
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
   print("Si ESTA FUNCIONANDO")
   
   if first_time == "":
      second_time = ""
      time_output.delete(0.0, "end")
      return
   
   first = time_selector1.get()
   second = time_selector2.get()
   second_time = eval(f"{first_time}{convertors[first][second]}")
   
   time_output.delete(0.0, "end")
   time_output.insert(0.0, second_time)
   
   
time_input = ctk.CTkTextbox(root, width=200, height=70, font=(('Roboto', 40)), corner_radius=1)
time_input.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

time_output = ctk.CTkTextbox(root, width=200, height=70, font=(('Roboto', 40)), corner_radius=1)
time_output.grid(row=1, column=0, columnspan=2, padx=5, pady=5)




time_selector1 = ctk.CTkOptionMenu(root, values=["Microseconds", "Milliseconds","Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"], command=time_eval())
time_selector1.grid(row=0, column=2, columnspan=5, padx=5, pady=5)
time_selector1.set("Hours")

time_selector2 = ctk.CTkOptionMenu(root, values=["Microseconds", "Milliseconds","Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"], command=time_eval())
time_selector2.grid(row=1, column=2, columnspan=5, padx=5, pady=5)
time_selector2.set("Minutes")



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