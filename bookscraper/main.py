import schedule
import time
import os

print("schduler initialzing")
schedule.every(3).seconds.do(lambda: os.system('scrapy crawl abookspider'))
print("next time run at" + str(schedule.next_run()))

while True:
    schedule.run_pending()
    time.sleep(1)