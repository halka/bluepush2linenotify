import sqlite3
import os
import requests
from datetime import datetime as dt

# now
now = dt.now()
nowdatetime = now.strftime('%Y-%m-%d %H:%M:%S')

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