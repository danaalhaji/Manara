import datetime
def daysbetweentwo(date1,date2):
    date1 = date1.replace("-","/")
    date2 = date2.replace("-","/")
    datetime1 = datetime.datetime.strptime(date1, '%Y/%m/%d')
    datetime2 = datetime.datetime.strptime(date2, '%Y/%m/%d')
    return abs(datetime1-datetime2)


print(daysbetweentwo("2019-06-29","2019-06-30"))