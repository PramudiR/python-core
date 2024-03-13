# Extract, convert and manage time data
from datetime import datetime

# Get date from the given Seconds
def seconds2Date(timeSeconds):
    d = datetime.utcfromtimestamp(timeSeconds)
    return d.strftime('%d %b, %Y')
