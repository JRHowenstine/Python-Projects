from datetime import datetime
import pytz

newYorkTz=pytz.timezone("America/New_York")
timeInNewYork=datetime.now(newYorkTz)
currentTimeInNewYork=timeInNewYork.strftime("%H")
if int(currentTimeInNewYork) >= 9 and int(currentTimeInNewYork) < 17:
    print("The New York branch is currently open")
else:
    print("The New York branch is currently closed")


londonTz=pytz.timezone("Europe/London")
timeInLondon=datetime.now(londonTz)
currentTimeInLondon=timeInLondon.strftime("%H")
if int(currentTimeInLondon) >= 9 and int(currentTimeInLondon) < 17:
    print("The London branch is currently open")
else:
    print("The London branch is currently closed")


portlandTz=pytz.timezone("America/Los_Angeles")
timeInPortland=datetime.now(portlandTz)
currentTimeInPortland=timeInPortland.strftime("%H")
if int(currentTimeInPortland) >= 9 and int(currentTimeInPortland) < 17:
    print("The Portland branch is currently open")
else:
    print("The Portland branch is currently closed")
