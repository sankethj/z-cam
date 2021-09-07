# Z-Cam

## INSTALLATION :
* `apt-get update`
* `apt-get upgrade`
* Install any [Python 3.x](https://docs.python-guide.org/starting/install3/linux/) version
* Make sure you are using **pip** of Python3
* `pip install Flask`
* `pip install pyngrok`
* `pip install datetime`
* `pip install pyfiglet`

### TESTED ON :
* Ubuntu
* Kali Linux
* Termux

## FEATURES :
* [+] Real camera hacking !
* [+] Python compatible
* [+] URL Masking
* [+] Less Size
* [+] Updated regularly

## USAGE :
`python3 zcam.py`

## HOW TO USE
- After running the script, you will be provided with **ngrok** tunnel link 
- Cam Images will be stored in the directory called capture.
- Captured Cam Image will be saved in the format of `img_<year-month-day> <time_24hr_format>.png`
- Clients' ip address, User-Agent (system, browser) details and it will be saved in the file called `myfile.txt`

## CONCEPT
- This tool is **Python** compatible
- It uses Flask to host web-server
- If you go through the code, there is both GET and POST requests made.
- GET request will provide you the Clients' ip address, User-Agent details and it will be saved in the file called myfile.txt
- POST request will provide you the Clients' Base64 encoded Cam image data and it will be decrypted and stored as image file in capture directory 
- I used pyngrok (the wrapper of ngrok), to create https tunnel.

