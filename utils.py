from datetime import datetime

def getTimestamp():
  now = datetime.now()
  return datetime.timestamp(now)