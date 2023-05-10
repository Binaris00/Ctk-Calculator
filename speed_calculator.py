import customtkinter as ctk
from convertors_template import Convertor_template

speed = Convertor_template(convertors_dict= {
    "Meters per second": {"Miles per hour": "*2.2369", "Kilometers per hour": "*3.6", "Feet per second": "*3.2808", "Knots": "*1.9438"},
    "Miles per hour": {"Meters per second": "/2.2369", "Kilometers per hour": "*1.6093", "Feet per second": "*1.4667", "Knots": "/1.1508"},
    "Kilometers per hour": {"Meters per second": "/3.6", "Miles per hour": "/1.6093", "Feet per second": "*0.9114", "Knots": "/1.852"},
    "Feet per second": {"Meters per second": "/3.2808", "Miles per hour": "/1.4667", "Kilometers per hour": "/0.9114", "Knots": "/1.6878"},
    "Knots": {"Meters per second": "/1.9438", "Miles per hour": "*1.1508", "Kilometers per hour": "*1.852", "Feet per second": "*1.6878"}
},
                           convertors_list=["Meters per second", "Miles per hour", "Kilometers per hour", "Feet per second", "Knots", "Knots"]
)

speed.mainloop()