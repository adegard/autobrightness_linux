# autobrightness_linux
automatically set linux brightness from webcam


# list monitor and substitute in the code

xrandr --listmonitors

# add in cron tab

crontab -e

DISPLAY=:0

*/5 * * * * /usr/bin/python3 /path/to/your/script.py >> /path/to/your/logfile.log 2>&1
