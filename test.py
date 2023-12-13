import datetime

now = datetime.date.today()
days = datetime.timedelta(days = 9)
past = now - days

past_day = "{0:%Y/%m/%d}".format(past)

day = "2022/12/03"

#print(past_day)
#print("2023/01/27" > past_day)
print(f"{day} > {past_day} = {day > past_day}")