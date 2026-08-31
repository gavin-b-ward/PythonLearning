from datetime import datetime, date

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second

print(day, month, year, hour, minute, second)

print(datetime.strftime(now, "%m/%d/%Y, %H:%M:%S"))

string = "Today is 31 August, 2026"
print(datetime.strptime(string, "Today is %d %B, %Y"))
ny = datetime(2027, 1, 1)

time_till_new_year = ny - now
print(time_till_new_year)

utc = datetime(1970, 1, 1)
time_since_utc = now - utc
print(time_since_utc)
