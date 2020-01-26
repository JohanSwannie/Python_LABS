#  Date + Time - General uses

import datetime

print(dir(datetime))

johan_swan = datetime.date(1963, 8, 31)
print(johan_swan)

dt = datetime.timedelta(10)     #  Create 10 days to add to other date
print(dt + johan_swan)
print(johan_swan.strftime("%A, %B %d, %Y"))
msg = "Johan Swan was born in Kitwe Zambia on {:%A, %B %d, %Y}."
print(msg.format(johan_swan))

l_date = datetime.date(1971, 12, 4)
l_time = datetime.time(18, 33, 21, 160125)
l_datetime = datetime.datetime(1971, 12, 4, 18, 33, 21, 114162)
print(l_date, '  ',  l_time, '  ', l_datetime)
print(l_date.year, '  ', l_date.month, '  ', l_date.day)
print(l_time.hour, '  ', l_time.minute, '  ', l_time.second, '  ', l_time.microsecond)
print(datetime.datetime.today())

js_birth = "8/31/1963"
print(datetime.datetime.strptime(js_birth, "%m/%d/%Y" ))
