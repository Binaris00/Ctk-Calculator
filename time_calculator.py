import customtkinter as ctk
from convertors_template import Convertor_template

tm_calculator = Convertor_template(convertors_dict= {
   "Microseconds": {"Milliseconds":"/1000", "Seconds":"/1000000", "Minutes":"*0.000016666666666666668", "Hours":"*0.0000002777777777777778", "Days":"*0.000000011574074074074074", "Weeks":"*0.0000000016534391534391535", "Years":"*0.00000000003168876416355726"},
   "Milliseconds": {"Microseconds":"*1000", "Seconds":"/1000", "Minutes":"*0.000016666666666666668", "Hours":"*0.0000002777777777777778", "Days":"*0.000000011574074074074074", "Weeks":"*0.0000000016534391534391535", "Years":"*0.00000000003168876416355726"},
   "Seconds": {"Microseconds":"*1000000", "Milliseconds":"*1000", "Minutes":"/60", "Hours":"*0.0002777777777777778", "Days":"*0.000011574074074074074", "Weeks":"*0.0000016534391534391535", "Years":"*0.00000003168876416355726"},
   "Minutes": {"Microseconds":"*60000000", "Milliseconds":"*60000", "Seconds":"*60", "Hours":"/60", "Days":"*0.041666666666666664", "Weeks":"*0.005952380952380952", "Years":"*0.00011415525114155251"},
   "Hours": {"Microseconds":"*3600000000", "Milliseconds":"*3600000", "Seconds":"*3600", "Minutes":"*60", "Days":"/24", "Weeks":"*0.14285714285714285", "Years":"*0.0027397260273972603"},
   "Days": {"Microseconds":"*86400000000", "Milliseconds":"*86400000", "Seconds":"*86400", "Minutes":"*1440", "Hours":"*24", "Weeks":"/7", "Years":"*0.0027397260273972603"},
   "Weeks": {"Microseconds":"*604800000000", "Milliseconds":"*604800000", "Seconds":"*604800", "Minutes":"*10080", "Hours":"*168", "Days":"*7", "Years":"*0.05214285714285714"},
   "Years": {"Microseconds":"*31536000000000", "Milliseconds":"*31536000000", "Seconds":"*31536000", "Minutes":"*525600", "Hours":"*8760", "Days":"*365", "Weeks":"*52.14285714285714"}
},
                                   convertors_list=["Microseconds", "Milliseconds", "Seconds", "Minutes", "Hours", "Days", "Weeks", "Years"])

tm_calculator.mainloop()