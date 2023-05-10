import customtkinter as ctk
from convertors_template import Convertor_template

pressure = Convertor_template(convertors_dict={
    "Pascal": {
        "Bar": "/100000",
        "Pound per square inch": "/6895",
        "Kilopascal": "/1000",
        "Millibar": "/100",
        "Millimeter of mercury": "/133",
        "Atmosphere": "/101325"
    },
    "Bar": {
        "Pascal": "*100000",
        "Pound per square inch": "*14.504",
        "Kilopascal": "*100",
        "Millibar": "*1000",
        "Millimeter of mercury": "*750.062",
        "Atmosphere": "/1.013"
    },
    "Pound per square inch": {
        "Pascal": "*6895",
        "Bar": "/14.504",
        "Kilopascal": "*6.895",
        "Millibar": "*68.948",
        "Millimeter of mercury": "*51.715",
        "Atmosphere": "/14.696"
    },
    "Kilopascal": {
        "Pascal": "*1000",
        "Bar": "/100",
        "Pound per square inch": "/6.895",
        "Millibar": "*10",
        "Millimeter of mercury": "/7.501",
        "Atmosphere": "/101.325"
    },
    "Millibar": {
        "Pascal": "*100",
        "Bar": "/1000",
        "Pound per square inch": "/68.948",
        "Kilopascal": "/10",
        "Millimeter of mercury": "/1.333",
        "Atmosphere": "/1013.25"
    },
    "Millimeter of mercury": {
        "Pascal": "*133",
        "Bar": "/750.062",
        "Pound per square inch": "/51.715",
        "Kilopascal": "*7.501",
        "Millibar": "*1.333",
        "Atmosphere": "/760"
    },
    "Atmosphere": {
        "Pascal": "*101325",
        "Bar": "*1.013",
        "Pound per square inch": "*14.696",
        "Kilopascal": "*101.325",
        "Millibar": "*1013.25",
        "Millimeter of mercury": "*760"
    }
},
                              convertors_list=["Pascal", "Bar", "Pound per square inch", "Kilopascal", "Millibar", "Millimeter of mercury", "Atmosphere"]
)

pressure.mainloop()