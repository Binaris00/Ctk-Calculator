import customtkinter as ctk
from convertors_template import Convertor_template

vm_calculator = Convertor_template(convertors_dict={
   "Milliliters": {"Liters":"/1000", "US Teaspoons":"/4.929", "US Tablespoons":"/14.787", "US Fluid Ounces":"/29.574", "US Cups":"/236.588", "US Pints":"/473.176", "US Quarts":"/946.353", "US Gallons":"/3785.412"},
   "Liters": {"Milliliters":"*1000", "US Teaspoons":"*202.884", "US Tablespoons":"*67.628", "US Fluid Ounces":"*33.814", "US Cups":"*4.227", "US Pints":"*2.113", "US Quarts":"*1.057", "US Gallons":"*0.264"},
   "US Teaspoons": {"Milliliters":"*4.929", "Liters":"/202.884", "US Tablespoons":"/3", "US Fluid Ounces":"/6", "US Cups":"/48", "US Pints":"/96", "US Quarts":"/192", "US Gallons":"/768"},
   "US Tablespoons": {"Milliliters":"*14.787", "Liters":"/67.628", "US Teaspoons":"*3", "US Fluid Ounces":"/2", "US Cups":"/16", "US Pints":"/32", "US Quarts":"/64", "US Gallons":"/256"},
   "US Fluid Ounces": {"Milliliters":"*29.574", "Liters":"/33.814", "US Teaspoons":"*6", "US Tablespoons":"*2", "US Cups":"*0.125", "US Pints":"*0.0625", "US Quarts":"*0.03125", "US Gallons":"*0.0078125"},
   "US Cups": {"Milliliters":"*236.588", "Liters":"/4.227", "US Teaspoons":"*48", "US Tablespoons":"*16", "US Fluid Ounces":"*8", "US Pints":"*0.5", "US Quarts":"*0.25", "US Gallons":"*0.0625"},
   "US Pints": {"Milliliters":"*473.176", "Liters":"/2.113", "US Teaspoons":"*96", "US Tablespoons":"*32", "US Fluid Ounces":"*16", "US Cups":"*2", "US Quarts":"*0.5", "US Gallons":"*0.125"},
   "US Quarts": {"Milliliters":"*946.353", "Liters":"*1.057", "US Teaspoons":"*192", "US Tablespoons":"*64", "US Fluid Ounces":"*32", "US Cups":"*4", "US Pints":"*2", "US Gallons":"*0.25"},
   "US Gallons": {"Milliliters":"*3785.412", "Liters":"*0.264", "US Teaspoons":"*768", "US Tablespoons":"*256", "US Fluid Ounces":"*128", "US Cups":"*16", "US Pints":"*8", "US Quarts":"*4"}
},
                                   convertors_list=["Milliliters", "Liters", "US Teaspoons", "US Tablespoons", "US Fluid Ounces", "US Cups", "US Pints", "US Quarts", "US Gallons"])

vm_calculator.mainloop()