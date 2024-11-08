from datetime import datetime

def getCurrentTime():
    currentTime = datetime.now()
    strCurrentTime = currentTime.strftime('%Y%m%d_%H%M%S')
    return strCurrentTime
