#import toolforge
from helpers import daterange, date_from_iso, date_to_iso

def number_of_articles(project, startdate, enddate):
    res = {}
    for date in daterange(date_from_iso(startdate), date_from_iso(enddate)):
        res[date_to_iso(date)] = 100
    return res