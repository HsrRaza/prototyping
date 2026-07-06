from datetime import datetime , timedelta
from datetime import date



now = datetime.now()

# print(now)
# print(now.year)
# print(now.month)
# print(now.day)


# print()

# print(now.hour)
# print(now.minute)
# print(now.second)


today = date.today()
# print(today)


# print(now.time())
# print(now.strftime("%d/%m/%y"))


tommorow = today + timedelta(days=1)
# print(tommorow)



# otp expiry

expiry = datetime.now() + timedelta(minutes=5)
# print(expiry)

# subscriptions ends

expire = datetime.now() + timedelta(days=30)

# print(expire)


# logging

print(datetime.now())
