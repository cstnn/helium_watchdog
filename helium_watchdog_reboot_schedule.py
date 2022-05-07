"""
# If you just want to reboot at a time interval
# Configure your details and preferences in the "secrets.txt" file
cache_name= your hotspot animal name like "alert_shadow_iguana"
cache_address= your hotspot public blockchain address like "11q2UB9Cy9GsdHkHCn2K1F2LZLxDSfe9Xa4F3ir1NMfTZZ6bs7R"
cache_ip= your internal local IP like "192.168.1.4"
sleep= the number of seconds between checks like "7200"
"""


from functools import cache
import bobcat
import helium
from utilities import LogFile
import _gmail
import time
from datetime import datetime

from sqlalchemy import create_engine, table, column
import db_actions
import secrets
import telebot

secrets = db_actions.secrets()

verbose = secrets['verbose']
send_emails = secrets['send_emails']
send_tg_msg = secrets['send_telegram_msg']
tg_token = secrets['tg_token']
dry_run = secrets['dry_run']
cache_name = secrets['cache_name']
log = secrets['log']
email_to = secrets['email_to']
msg_to = secrets['msg_to']
sleep = int(secrets['sleep'])
# print(verbose)


#################################################

if log == 'True':
    LogFile.start()

# initialize()
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
if send_emails == 'True':
    _gmail.send_email(f"ECHO watchdog started at {dt_string}", f"""Hi,\nI'm ECHO the watchdog for your BOBCAT 300 {secrets['cache_name']}.\nEvery {int(secrets['sleep'])/60/60} hours I will check the status.\nIf something important happens I will bark and send you an email.""", email_to)
    if verbose == 'True':
        print(f"   {dt_string} Sending email ...")

if send_tg_msg == 'True':
    tb.send_message(msg_to, f"""Hi,\nI'm ECHO the watchdog for your BOBCAT 300 {secrets['cache_name']}.\nEvery {int(secrets['sleep'])/60/60} hours I will check the status.\nIf something important happens I will bark and send you an email.""")
    if verbose == 'True':
        print(f"   {dt_string} Sending Telegram message ...")

global iteration
iteration = 0
print("=====================================================")
print(f":: MONITORING session in a {sleep/60/60} hours loop ::")
print("=====================================================")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(f":::::: Starting LOOP at {dt_string}")

ip = secrets['cache_ip']

try:
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        time.sleep(sleep) # sleeping first as is good for your health :)
        
        if dry_run == 'False':
            if verbose == 'True':
                print(f"   {dt_string} Regular reboot based on schedule >>>>> REBOOTING <<<<<")
            bobcat.bobcat_reboot(ip)
        

        iteration += 1
        if verbose == 'True':
            print(f":::::: {dt_string} Going to sleep for {sleep / 60} minutes")
        time.sleep(sleep)

except Exception as ex:
    if verbose == 'True':
            print(f"   {dt_string} ERROR the loop \n{ex}")
finally:
    if log == 'True':
        LogFile.close()
