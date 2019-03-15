from datetime import datetime, timedelta

def date_to_iso(obj_date):
    return obj_date.strftime('%Y%m%d')

def date_from_iso(str_date):
    return datetime.strptime(str_date, '%Y%m%d')

def daterange(start_date, end_date):
    end_date += timedelta(1)
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)