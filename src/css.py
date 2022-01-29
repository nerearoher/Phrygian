BLUE_MIST = '#90AFC5'
BLUE_MIST_2 = '#79C8FF'
BLUE_STONE = '#336B87'
GREY_SHADOW = '#2A3132'
RED_AUTUM = '#763626'

PHRYGIAN_GUI = f"""
* {{
    color: {BLUE_MIST_2};
    background: {BLUE_MIST};
}}

QPushButton {{
    background-color: {BLUE_STONE};
    border-width: 2px;
    border-radius: 5px;
    border-color: beige;
    font: 18px;
    padding: 5px;
    width: 10px;
	height: 80px;
}}

QPushButton:hover {{
    background: {RED_AUTUM};
    color: {GREY_SHADOW}
}}

QPushButton:pressed {{
    background: {RED_AUTUM};
    color: {GREY_SHADOW}
}}

#label_welcome {{
    color: #2A3132;
    font: bold 40px;
    border: 2px;
    border-radius: 4px;
    padding: 2px;
}}

QLabel {{
    color: #2A3132;
    font: 20px;
    border: 2px;
    border-radius: 4px;
    padding: 2px;
}}

#QFormLayout {{
    color: {GREY_SHADOW};
    background-color: {BLUE_MIST};
}}

"""