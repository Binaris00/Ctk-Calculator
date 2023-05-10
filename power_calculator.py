import customtkinter as ctk
from convertors_template import Convertor_template

power = Convertor_template(convertors_dict={
    "Watts": {
        "Kilowatts": "/1000",
        "Megawatts": "/1000000",
        "Gigawatts": "/1000000000",
        "Horsepower": "*0.00134102209"
    },
    "Kilowatts": {
        "Watts": "*1000",
        "Megawatts": "/1000",
        "Gigawatts": "/1000000",
        "Horsepower": "*1.3404825737"
    },
    "Megawatts": {
        "Watts": "*1000000",
        "Kilowatts": "*1000",
        "Gigawatts": "/1000",
        "Horsepower": "*1341.022089595"
    },
    "Gigawatts": {
        "Watts": "*1000000000",
        "Kilowatts": "*1000000",
        "Megawatts": "*1000",
        "Horsepower": "*1341022.089595"
    },
    "Horsepower": {
        "Watts": "*745.699872",
        "Kilowatts": "*0.745699872",
        "Megawatts": "/1341.022089595",
        "Gigawatts": "/1341022.089595"
    }
},
                           convertors_list=["Watts", "Kilowatts", "Kilowatts", "Megawatts", "Gigawatts", "Horsepower"]
)

power.mainloop()