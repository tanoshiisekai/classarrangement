from datetime import datetime
from datetime import timedelta
import os


def cleaner():
    tdel = timedelta(days=5)
    lasttime = (datetime.now() - tdel).strftime("%Y%m%d")
    loglist = os.listdir("logs")
    loglist = [x for x in loglist if x[:8] < lasttime]
    for ll in loglist:
        os.remove("logs/" + ll)


cleaner()
