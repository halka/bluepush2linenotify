# -*- coding: UTF-8 -*-
import os

# now


def now():
    from datetime import datetime as dt
    now = dt.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')


def playMp3(path, freq, duration):
    import pygame.mixer
    import time
    # It is necessary to change the frequency according to the frequency of the audio file.
    pygame.mixer.init(frequency=freq)
    # Path to sound file.
    pygame.mixer.music.load(path)
    # Count of play the sound file..
    pygame.mixer.music.play(1)
    # Time to play.
    time.sleep(duration)
    pygame.mixer.music.stop()


def playWave(path):
    import subprocess
    subprocess.call('aplay ' + path, shell=True)

# db


def insertDB(dbfile, message):
    import sqlite3
    con = sqlite3.connect(dbfile)
    c = con.cursor()
    c.execute("insert into report values (?)", (message,))
    con.commit()
    con.close()

# LINE Notify


def LineNofify(message):
    import requests
    endpoint = 'https://notify-api.line.me/api/notify'
    token = os.getenv('LINE_NOTIFY_TOKEN')
    headers = {"Authorization": "Bearer " + token}
    payload = {"message":  message}
    requests.post(endpoint, headers=headers, params=payload)


def main():
    nowdatetime = now()
    playMp3(os.path.abspath(os.path.dirname(__file__)) +
            "/nc100421.mp3", 48000, 3)
    insertDB(os.path.abspath(os.path.dirname(__file__)) +
             "/report.db", nowdatetime)
    LineNofify(nowdatetime)


if __name__ == '__main__':
    main()
