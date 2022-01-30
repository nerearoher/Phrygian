BROWN_MIST = '#D9C8C0'
GREY_SHADOW = '#2A3132'
RED_AUTUM = '#763626'
BROWN = '#AD857C'
GREY_MIST = '#E8E8E8'


PHRYGIAN_GUI = f"""
* {{
    color: {GREY_SHADOW};
    background: {GREY_MIST};
    text-align:center;
}}

QPushButton {{
    color: black;
    background-color: {BROWN};
    border-width: 2px;
    border-width: 10px;
    border-radius: 10px;
    font: bold 18px;
    padding: 5px;
    width: 600px;
	height: 40px;
    text-align:center;
}}

QDialogButtonBox QPushButton {{
    color: black;
    background-color: {BROWN};
    border-width: 2px;
    border-width: 10px;
    border-radius: 10px;
    font: bold 15px;
    padding: 5px;
    width: 80px;
	height: 25px;
    text-align:center;
}}

QPushButton:hover {{
    background: {BROWN_MIST};
    color: {RED_AUTUM};
    font: bold;
    border-radius: 10px;
    border :2px solid ;
    border-top-color : {RED_AUTUM};
    border-left-color : {RED_AUTUM};
    border-right-color : {RED_AUTUM};
    border-bottom-color : {RED_AUTUM};
    text-align:center;
}}

QPushButton:pressed {{
    text-align:center;
    background: {RED_AUTUM};
    color: {GREY_SHADOW}
}}

#label_welcome {{
    text-align:center;
    color: #2A3132;
    font: bold 40px;
    border: 2px;
    border-radius: 4px;
    padding: 2px;
}}

#BrowserButton {{
    color: black;
    background-color: {BROWN};
    border-width: 2px;
    border-width: 10px;
    border-radius: 10px;
    font: bold 15px;
    padding: 5px;
    width: 600px;
	height: 25px;
    text-align:center;
}}

#BrowserButton:hover {{
    background: {BROWN_MIST};
    color: {RED_AUTUM};
    font: bold 15px;
    border-radius: 10px;
    border :2px solid ;
    border-top-color : {RED_AUTUM};
    border-left-color : {RED_AUTUM};
    border-right-color : {RED_AUTUM};
    border-bottom-color : {RED_AUTUM};
    text-align:center;
}}

#BrowserButton:pressed {{
    text-align:center;
    background: {RED_AUTUM};
    color: {GREY_SHADOW}
}}

QLabel {{
    text-align:center;
    color: #2A3132;
    font: 20px;
    border: 2px;
    border-radius: 4px;
    padding: 2px;
}}

QLineEdit {{  
    border: 0px solid; 
    background-color: {0}; 
    color: black;
    font-size: 15px;
    width: 700px;
	height: 30px;
}} 

QLineEdit:hover {{ 
    border: 1px solid #763626;
}}

QComboBox {{
    border: 0px solid; 
    background-color: {0}; 
    color: black;
    font-size: 18px;
}}

QComboBox:hover {{ 
    border: 1px solid #763626; 
}}

QSpinBox {{
    border: 0px solid; 
    background-color: {0}; 
    color: black;
    font-size: 18px;
}}

QSpinBox:hover {{ 
    border: 1px solid #763626; 
}}

"""
