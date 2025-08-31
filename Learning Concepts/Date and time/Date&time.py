
import datetime

date = datetime.date(day=26,month=4,year=2007)
today = datetime.date.today()

time = datetime.time(12,17,20)


#datetime data type to string
current_time = datetime.datetime.now()    #datetime is also a class
current_time = current_time.strftime(f"Current time:%H:%M:%S \n{date}\nCurrent date:{today}\nor\nCurrent date:%d-%m-%y")


#String data type to datetime
user_string = "22:04:40"
user_time = datetime.datetime.strptime(user_string , "%H:%M:%S").time() # The .time() returns the time part only while date() gives date only

print(user_time)
current_time = datetime.strptime(current_time ,  "%H:%M:%S") #strptime changes string to datetime format


print(current_time)
