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
ketik (W +  " Hotmail Email Checker 2020 🤖 ")
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

