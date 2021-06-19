from datetime import datetime,timedelta

def invertal_dates(start_day,end_day):
    d1 = datetime.strptime(start_day,'%Y%m%d')
    d2 = datetime.strptime(end_day,'%Y%m%d')
    new_start_date = find_day(d1)
    for each_saturday in saturdays_generator(new_start_date,d2):
        if is_fourth_saturday(each_saturday) ^ is_a_multiple_of_5(each_saturday):
            print(datetime.strftime(each_saturday,'%Y%m%d'))

def is_fourth_saturday(given_day):
    if given_day.day in [29,30,31]:
        return False
    elif given_day.day >= 22:
        return True
    return False

def is_a_multiple_of_5(given_date):
    if (given_date.day) % 5 == 0:
        return True
    return False


def saturdays_generator(given_start_date,given_end_date):
    curr_date = given_start_date
    delta = timedelta(days=7)
    while curr_date <= given_end_date:
        yield curr_date
        curr_date = curr_date + delta

def find_day(start_date):
    diff_day = {"0":5,"1":4,"2":3,"3":2,"4":1,"6":6}
    day = start_date.weekday()
    if day == 5:
        return start_date
    delta = timedelta(days=diff_day[str(day)])
    new_start_day = start_date + delta
    return new_start_day

invertal_dates("20180728","20180927")
