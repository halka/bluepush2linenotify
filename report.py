# -*- coding: UTF-8 -*-
import sqlite3
import os
import requests
import pygame.mixer
import time
from datetime import datetime as dt

# now
now = dt.now()
nowdatetime = now.strftime('%Y-%m-%d %H:%M:%S')

# sound
# It is necessary to change the frequency according to the frequency of the audio file.
pygame.mixer.init(frequency = 48000)
# Path to sound file. 
pygame.mixer.music.load(os.path.abspath(os.path.dirname(__file__))+"/hoge.mp3")
# Count of play the sound file..
pygame.mixer.music.play(1)
# Time to play.
time.sleep(3)
pygame.mixer.music.stop()

# db
con = sqlite3.connect(os.path.abspath(os.path.dirname(__file__))+"/report.db")
c = con.cursor()
c.execute("insert into report values (?)",(nowdatetime,))
con.commit()
con.close()

# LINE Notify
endpoint = 'https://notify-api.line.me/api/notify'
token = os.getenv('LINE_NOTIFY_TOKEN')
headers = {"Authorization" : "Bearer "+ token}

message = nowdatetime
payload = {"message" :  message}
r = requests.post(endpoint ,headers = headers ,params=payload)