from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return {"data": "Hello Flask!"}

@app.route('/current_datetime', methods=['GET'])
def current_datetime():
    message = "" 
    if int(datetime.now().strftime("%H")) < 12:
        message = "Bom dia!"
    elif int(datetime.now().strftime("%H")) < 18:
        message = "Boa tarde!"
    else:
        message = "Boa noite!"
    
    return {
        "current_datetime": datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"),
        "message": message,
        }
