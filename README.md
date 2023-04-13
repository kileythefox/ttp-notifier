# ttp-notifier
Simple script to alert a Discord webhook when appointments are available at a CBP Global Entry or NEXUS enrollment center.

## Installation
1. Install Python3 (https://www.python.org/downloads/) and (optional) Git.
2. Install requests using ```pip3 install requests```
3. Clone this repository (```git clone https://github.com/kileythefox/ttp-notifier```) or otherwise download to your machine.
4. Determine the ID number of your desired Enrollment Center.  
5. Populate the variable WEBHOOK_URL with a Discord Webhook URL and the variable LOCATION_IDS with a List containing the ID numbers of your desired Enrollment Centers.
6. Execute the script with ```python3 run.py``` (```python run.py``` on some systems)
7. Enjoy!

## Determining the ID Number of an Enrollment Center
1. Visit (https://ttp.cbp.dhs.gov/schedulerui/schedule-interview/location?lang=en&vo=true)
2. Open Inspect Element (Developer Tools) in your favorite web browser.  Click "Network" at the top.
3. Click on the name of your desired location on the DHS website.
4. A request should populate to the endpoint "slot-availability".  Look at the URL.  The location ID will be passed in the GET parameter "locationId" (i.e slot-availability?locationId=5032)

## Enrollment Centers
| Location  | ID |
| ------------- | ------------- |
| Edmonton International Airport  | 5032  |
| Calgary International Airport  | 5030  |
| Atlanta International Global Entry EC | 5182 | 
