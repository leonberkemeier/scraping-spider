from datetime import datetime 
from datetime import date,time
import datetime


# today = date.today()
# time = datetime.now()
# time = time.now()

# date = datetime.date.today()
date = datetime.date.today()

print("current date : ", date)

# print('date is : ', today)

# print(time)

import sys

# print(sys.executable)

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print('now', now)
