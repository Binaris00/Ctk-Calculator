import customtkinter as ctk
from convertors_template import Convertor_template

tm_calculator = Convertor_template(convertors_dict={
   "Celsius": {"Fahrenheit":"*1.8+32", "Kelvin":"+273.15"},
   "Fahrenheit": {"Celsius":"(/1.8)-32", "Kelvin":"(/1.8)-32+273.15"},
   "Kelvin": {"Celsius":"-273.15", "Fahrenheit":"-459.67+1.8"},
},
                                   convertors_list=["Celsius", "Fahrenheit", "Kelvin"])

tm_calculator.mainloop()