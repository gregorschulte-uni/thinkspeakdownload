# -*- coding: utf-8 -*-
"""
Automated CSV Download from Thingspeak for Data-Import
Gregor Schulte 2021.03.02

"""

import requests
import datetime
from calendar import monthrange

fields = [892674,1103937,1103934,1103936,1136636]
names  = ["Med9", "Zeb2","Atl2-R","Pac6-R","Ind5-R"]

now = datetime.datetime.now()

year = int(now.strftime("%Y"))
month = int(now.strftime("%m"))

if month == 1:
    getMonth = 12
    getYear = year - 1
else:
    getMonth = month -1
    getYear = year
    
daysInGetMonth = monthrange(getYear,getMonth)[1]

for count, field  in enumerate(fields):
    
    getUrl = "https://api.thingspeak.com/channels/" + str(field) + "/feeds.csv?start=" + str(getYear) + "-" + str(getMonth).zfill(2) + "-01%2000:00:00&end=" + str(getYear) + "-" + str(getMonth).zfill(2) + "-" + str(daysInGetMonth).zfill(2) + "%2023:59:59"

    print(getUrl)
    
    filename = str(getYear) + "." + str(getMonth).zfill(2) + ". " + str(names[count]) + ".csv"

    r = requests.get(getUrl, allow_redirects=True)

    open("c:\\test\\"+filename, 'wb').write(r.content)