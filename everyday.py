import schedule
import time

def job():
    print("I'm working...")

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
schedule.clear()
schedule.every().day.at("00:36").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)