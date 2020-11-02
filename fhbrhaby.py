## fmbrute.py - Facebook Multi Brute Force
# -*- coding: utf-8 -*-
##
import os
import sys
import hashlib
import requests

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")

__banner__ = """\033[1;33m |\   /| FMBrhaby - Hotmail mail Brute Force
  \|_|/  Author: ArHaBy*
  /. .\  Version: 3.0v
 =\_Y_/= Telegram: @ciku370
  {>o<}  Insta: @ali.rhaby

=============================================="""
print(__banner__)

print ('              1-FHBrhaby-Hotmail')
print("")
print('==============================================')
print("===============ارهابي_عليه_السلام==============")
print('==============================================')
print("")
print ('              2- DeveloperMaker ')
print('==============================================')


ali1 = input ("")
if ali1 == '1' :
        import requests
        import sys
        from bs4 import BeautifulSoup
        import json
        import webbrowser
        import os
        from colorama import Fore
        from time import sleep
        W = "\033[96m"
        green_color = "\033[1;32m"
        print("")


        def ketik(s):
                for ASU in s + '\n':
                        sys.stdout.write(ASU)
                        sys.stdout.flush()
                        sleep(50. / 1000)

        os.system('clear')

        print (' ')
        ketik (" FHBrhaby-Hotmail Email Brute Force 2020 ")
        sleep(0.5)
        print("")


        def hotmail():
            ss = input ('Enter list email  -> ')
            bpass = open (ss, 'r').read ().splitlines ()
            for password in bpass:
                aaa = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + password + "&_=1604288577990"
                payload = ''
                headers = {
                                "Accept": "*/*",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                                "Connection": "close",
                                "Host": "odc.officeapps.live.com",
                                "Accept-Encoding": "gzip, deflate",
                                "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
                                "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
                                "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
                                "uaid": "d06e1498e7ed4def9078bd46883f187b",
                                "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
                            }
                response = requests.get (aaa, data=payload, headers=headers)
                if 'MSAccount' in response.text:
                    print (' -' * 15)
                    print (Fore.YELLOW +'Sorry, not Available : ' + password)
                elif "Neither" in response.text:
                    print (' -' * 15)
                    print (green_color + 'Available : ' + password)
                    with open ('Available.txt', 'a') as x:
                                x.write (password + '\n')
                    print (' -' * 15)
                    print ("")






        if __name__ == '__main__':
            hotmail()


if ali1 == '2' :
    import random
    import sys
    import os
    import time
    os.system("rm list.txt")
    print('=========================================')
    print('$Example Domain email')
    print('1-   @gmail.com')
    print('1-   @hotmail.com')
    print('1-   @yahoo.com')
    print('1-   @outlook.com')
    print('=========================================')
    print("")
    print ("$Example type ABC 123 ._ ")
    print ("1234567890qwertyuiopasdfghjklzxcvbnm._")
    print('================ letsgo ================')
    print("")
    #================================================
    uesr = input('username =ã€‹ã€‹ ')
    print('=========================================')
    rhaby1 = input('type ABC 123 ._ =ã€‹ã€‹ ')
    print('=========================================')
    email = input('Domain email =ã€‹ã€‹ ')
    print('=========================================')
    rhaby = input('What is a number List=ã€‹ã€‹ ')
    rhaby = int(rhaby)
    print('=========================================')
    rhaby2 = input('Number of mattresses=ã€‹ã€‹ ')
    rhaby2 = int(rhaby2)
    print('==================================')

    for password in range(rhaby):
        password = ''


        for item in range(rhaby2):
             rhaby3 = ''
        for item in range(rhaby2):
            rhaby3 += random.choice(rhaby1)



        print (uesr+rhaby3+email)
        with open('list.txt', 'a') as x:
         x.write(uesr + rhaby3 + email + '\n')
