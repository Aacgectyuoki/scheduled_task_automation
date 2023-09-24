# type in 'pip install apscheduler' in a shell before the following below

import subprocess
import time
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone  # Import the timezone module from the pytz library

# Define a timezone (e.g., Eastern Standard Time - EST)
est = timezone('US/Eastern')

# Function to open a Google Drive link in Chrome
def open_drive_link(link):
    subprocess.Popen(['open', '-a', 'Google Chrome', link])

# Create a scheduler with the specified timezone
scheduler = BackgroundScheduler(timezone=est)

# Schedule the opening of each link at the specified times in EST
# Run the schedule when you start your workday
scheduler.add_job(open_drive_link, 'cron', hour=10, minute=0, args=['https://docs.google.com/document/d/...'])  # Task at 10:00 AM EST
scheduler.add_job(open_drive_link, 'cron', hour=11, minute=0, args=['https://docs.google.com/document/d/...'])  # Task at 11:00 AM EST
scheduler.add_job(open_drive_link, 'cron', hour=17, minute=0, args=['https://docs.google.com/document/d/...'])  # Task at 5:00 PM EST

# Start the scheduler
scheduler.start()

# Keep the script running
try:
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()