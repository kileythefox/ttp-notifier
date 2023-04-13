WEBHOOK_URL = "" #URL of Discord webhook
LOCATION_IDS = ["5032"] #ID number(s) of enrollment center to query

import requests
import smtplib, ssl
import time
from datetime import datetime

def sendDiscordAlert(message):
    data ={
        "content": message
    }
    p = requests.post(WEBHOOK_URL, json = data)

announcedDates = []

while True:
    try:
        for x in range(0, len(LOCATION_IDS)):
            q = requests.get("https://ttp.cbp.dhs.gov/schedulerapi/slot-availability?locationId="+LOCATION_IDS[x])
            data = q.json()

            numSlots = len(data["availableSlots"])
            if numSlots > 0:
                for slot in data["availableSlots"]:
                    apptDate = slot["startTimestamp"]
                    readableDate = datetime.strptime(apptDate, "%Y-%m-%dT%H:%M").strftime("%A %Y-%m-%d %H:%M")
                    if(apptDate not in announcedDates):
                        sendDiscordAlert("APPOINTMENT IS AVAILABLE AT YEG\n"+readableDate)
                        print(readableDate)
                        announcedDates.append(apptDate)
            else:
                announcedDates = []
                print("No appointments found.")

        time.sleep(15)
    except Exception as e:
        print("EXCEPTION")
        print(e)
        print("Will retry in 30s..")
        time.sleep(30)
