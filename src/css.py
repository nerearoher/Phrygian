BLUE_MIST = '#D9C8C0'
BLUE_MIST_2 = '#79C8FF'
BLUE_STONE = '#DAD8D9'
GREY_SHADOW = '#2A3132'
RED_AUTUM = '#763626'

PHRYGIAN_GUI = f"""
* {{
    color: {BLUE_MIST_2};
    background: {BLUE_MIST};
    text-align:center;
}}

QPushButton {{
    color: black;
    background-color: {BLUE_STONE};
    border-width: 2px;
    border-width: 10px;
    border-radius: 10px;
    font: bold 18px;
    padding: 5px;
    width: 100px;
	height: 80px;
    text-align:center;
}}

QPushButton:hover {{
    background: {BLUE_MIST};
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

QLabel {{
    text-align:center;
    color: #2A3132;
    font: 20px;
    border: 2px;
    border-radius: 4px;
    padding: 2px;
}}
"""