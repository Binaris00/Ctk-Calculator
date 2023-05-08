import customtkinter as ctk
from convertors_template import Convertor_template

dt_calculator = Convertor_template(convertors_dict={
   "Bytes": {"Kilobytes":"/1024", "Megabytes":"/1048576", "Gigabytes":"/1073741824", "Terabytes":"/1099511627776", "Petabytes":"/1125899906842624"},
   "Kilobytes": {"Bytes":"*1024", "Megabytes":"/1024", "Gigabytes":"/1048576", "Terabytes":"/1073741824", "Petabytes":"/1099511627776"},
   "Megabytes": {"Bytes":"*1048576", "Kilobytes":"*1024", "Gigabytes":"/1024", "Terabytes":"/1048576", "Petabytes":"/1073741824"},
   "Gigabytes": {"Bytes":"*1073741824", "Kilobytes":"*1048576", "Megabytes":"*1024", "Terabytes":"/1024", "Petabytes":"/1048576"},
   "Terabytes": {"Bytes":"*1099511627776", "Kilobytes":"*1073741824", "Megabytes":"*1048576", "Gigabytes":"*1024", "Petabytes":"/1024"},
   "Petabytes": {"Bytes":"*1125899906842624", "Kilobytes":"*1099511627776", "Megabytes":"*1073741824", "Gigabytes":"*1048576", "Terabytes":"*1024"},
},
                                   convertors_list=["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"]
)

dt_calculator.mainloop()