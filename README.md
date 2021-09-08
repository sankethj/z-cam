# ZCam
Hack webcam using python by sending malicious link.

<p align="center">
<a href="https://github.com/sankethj/z-cam/"><img title="Tool" src="https://img.shields.io/badge/Tool-ZCam-green.svg?style=for-the-badge"></a>
<a><img title="Version" src="https://img.shields.io/badge/Version-2.0-green.svg?style=for-the-badge"></a>
<a><img title="Maintainence" src="https://img.shields.io/badge/Maintenance-Yes-green.svg?style=for-the-badge"></a>
</p>

![logo](/Images/logo.png)
  
## FEATURES :
* [+] Real-time Camera hacking
* [+] Python compatible
* [+] URL Shortener using bitly   [V 2.0]
* [+] Less Size
* [+] Updated regularly

## TESTED ON :
* Ubuntu
* Kali Linux
* Termux

## INSTALLATION :
* Install any [Python 3.x](https://docs.python-guide.org/starting/install3/linux/) version
* Make sure you are using **pip** of Python3, to check `pip --version`
* `git clone https://github.com/sankethj/z-cam`
* `pip install Flask`
* `pip install pyngrok`
* `pip install datetime`
* `pip install pyfiglet`
* `pip install pyshorteners`

## HOW TO USE :
- You need to signup in [Bitly](https://bitly.com/a/sign_up) and get your **access token** in API session
- Now in the project directory there is a file called `tokensbitly.py`, in that replace `your_token` with your access token
- After running the script, it will ask if you want to shorten the ngrok link type `y` or else type `n`
- you will be provided with **ngrok** tunnel link with or without shortened depending on what yoy have choosen
- Send that link to Client 
- Cam Images will be stored in the directory called capture.
- Captured Cam Image will be saved in the format of `img_<year-month-day> <time_24hr_format>.png`
- Clients' ip address, User-Agent (system, browser) details and it will be saved in the file called `myfile.txt`
- Make sure you use Wifi or Hotspot turned ON while using this tool.

## USAGE :
* `python3 zcam.py`
- **First time while running the tool, you need to start and test yourself. Most of time due to some problem in flask it wont take images properly. After getting tunneling link quit the program and start it again. It will work fine definitely.**

## CONCEPT :
- This tool is **Python** compatible
- It uses Flask to host web-server
- If you go through the code, there is both GET and POST requests made.
- GET request will provide you the Clients' ip address, User-Agent details and it will be saved in the file called myfile.txt
- POST request will provide you the Clients' Base64 encoded Cam image data and it will be decrypted and stored as image file in capture directory 
- I used pyngrok (the wrapper of ngrok), to create https tunnel and bitly to shorten the tunneled URL

## SCREENSHOTS :
* Replace with your bitly access token here 

![token](/Images/token1.jpg)
<br></br>
* Working of `zcam.py`

![tool1](/Images/tool1.png)
<br></br>
* Captured Cam image files

![tool2](/Images/tool2.png)
<br></br>
* A Sample crypto webpage which attract more client for free crypto

![webpage](/Images/webpage.png)
<br></br>
* Files stored

![files](/Images/final1.jpg) 
<br></br>

## YOUTUBE :
[![YOUTUBE](/Images/imageonline-co-logoadded.png)](https://www.youtube.com/embed/oy1LLH7Wt_4)

## CONTACT :
[![Telegram](https://img.shields.io/badge/TELEGRAM-Team_ETF-blue?style=for-the-badge&logo=telegram)](https://t.me/Team_ETF)
[![Twitter](https://img.shields.io/badge/TWITTER-SANKETH-blue?style=for-the-badge&logo=twitter)](https://twitter.com/SankethZ4N)
<a href="https://www.youtube.com/channel/UCJnx0yDhcTLWM3ZrAtSvaIw"><img title="YouTube" src="https://img.shields.io/badge/YouTube-Team ETF-blue?style=for-the-badge&logo=Youtube"></a>

## REFERENCES :
- [Musa](https://stackoverflow.com/users/1353011/musa) 
- Saycheese (thelinuxchoice)

## WARNING : 
**This tool is only for educational purposes. If you use this tool for other purposes except educational we will not be responsible in such cases.**

