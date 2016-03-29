import bs4
import requests
import smtplib
import os
import socket,sys,getpass

def take_new_pass():
    try:
        page=requests.get("http://www.vpnbook.com/freevpn")
        soup=bs4.BeautifulSoup(page.content,"html.parser")
        PASS=soup.find_all("strong")
        current_pass=PASS[6].text+"\n"+PASS[7].text
        f=open("UP.txt","r+")
        last_pass=f.read()
        f.close()
        print(last_pass,current_pass)
        if not last_pass==current_pass:
            os.remove("UP.txt")
            f=open("UP.txt","w")
            f.close()
            f=open("UP.txt","r+")
            f.write(current_pass)
            f.close()
            send_mail(current_pass)
    except Exception as e:
        print(e)

def send_mail(current_pass):
    try:
        smtpserver=smtplib.SMTP('smtp.gmail.com',587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        print('Connection to Gmail Successefully')
        print('Connected to Gmail'+'\n')
        try:
            gmail_user="my gmail@gmail.com"
            gmail_pass="my Password"
            smtpserver.login(gmail_user,gmail_pass)
            print("Login is Successefully")
        except Exception as e:
            print("Authentication faild"+"\n")
            print(e)
            smtpserver.close()

    except Exception as e:
        print("Connection to Gmail faild")
        print(e)

    to="my yahoo mail@yahoo.com"
    sub="VPN Pass"
    body=current_pass
    header="To:"+to+"\n"+"From:"+gmail_user+"\n"+"Subject:"+sub+"\n"
    msg=header+"\n"+body+"\n"

    try:
        smtpserver.sendmail(gmail_user,to,msg)
    except Exception as e:
        print(e)

take_new_pass()
