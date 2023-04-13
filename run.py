WEBHOOK_URL = "" #URL of Discord webhook
LOCATION_IDS = ["5032"] #ID number(s) of enrollment center to query
LOCATION_NICKNAMES = ["YEG"] #Nicknames that correspond to location IDs above

import requests
import time
from datetime import datetime

def sendDiscordAlert(message):
    data ={
        "content": message
    }
    p = requests.post(WEBHOOK_URL, json = data)

#create announcedDates 2D array and populate with correct number of locations
announcedDates = []
for x in range(0, len(LOCATION_IDS)):
    announcedDates.append([])

print("Checking for appointments...")

while True:
    try:
        for x in range(0, len(LOCATION_IDS)):
            #Request data from schedulerapi
            q = requests.get("https://ttp.cbp.dhs.gov/schedulerapi/slot-availability?locationId="+LOCATION_IDS[x])
            data = q.json()

            numSlots = len(data["availableSlots"])
            if numSlots > 0:
                for slot in data["availableSlots"]:
                    apptDate = slot["startTimestamp"]
                    readableDate = datetime.strptime(apptDate, "%Y-%m-%dT%H:%M").strftime("%A %Y-%m-%d %H:%M")

                    #If appointment has not been sent to Discord, do it!
                    if(apptDate not in announcedDates[x]):
                        print("Appointment found on "+readableDate+" at "+LOCATION_NICKNAMES[x])
                        sendDiscordAlert("APPOINTMENT IS AVAILABLE AT "+LOCATION_NICKNAMES[x]+"\n"+readableDate)
                        announcedDates[x].append(apptDate)
            else:
                #Reset announced dates
                announcedDates[x] = []

        time.sleep(15)
    except Exception as e:
        print("EXCEPTION")
        print(e)
        print("Will retry in 30s..")
        time.sleep(30)
