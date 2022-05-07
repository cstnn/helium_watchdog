import bobcat
import helium
import _gmail
from utilities import LogFile

import time
from datetime import datetime

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
cache_address = secrets['cache_address']
log = secrets['log']
email_to = secrets['email_to']
msg_to = secrets['msg_to']
sleep = int(secrets['sleep'])
# print(verbose)

cache_last_beacon = '1000000000'

# Check for stale hotspot
def beacon_check(address = secrets['cache_address'], ip=secrets['cache_ip']):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    last_beacon = helium.get_hotspot_beacon(secrets['cache_address'])
    last_beacon_date_time = last_beacon['last_beacon_date_time']
    if last_beacon['status_code'] == 200:
        if int(last_beacon_date_time) > int(cache_last_beacon) and int(cache_last_beacon) != 1000000000: # v1.1 fix to avoid reboot when starting the script for the 1st time as the new Beacont time value will always be higher than 1000000000
            if dry_run == 'False':
                if verbose == 'True':
                    print(f"   {dt_string} Updated last Beacont to : {int(last_beacon_date_time)}")
                bobcat.bobcat_reboot(ip)
                time.sleep(30)
            else:
                if verbose == 'True':
                    print(f"   {dt_string} Updated last Beacont to : {int(last_beacon_date_time)}")
            
            if send_emails == 'True':
                _gmail.send_email("Hotspot Restarted after BEACON", f"""{dt_string}\n{cache_name}\nHotspot was restarted after a BEACON) \n>>>>> REBOOTING <<<<<""", email_to)
                if verbose == 'True':
                    print(f"   {dt_string} Sending email ...")
            if send_tg_msg == 'True':
                tb.send_message(msg_to, f"""{dt_string}\n{cache_name}\nHotspot was restarted after a BEACON) \n>>>>> REBOOTING <<<<<""")
                if verbose == 'True':
                    print(f"   {dt_string} Sending Telegram message ...")
    else:
        if verbose == 'True':
            print(f"   {dt_string} Helium API not responding")
# stale_check()

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
try:
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        
        
        #####
        if verbose == 'True':
            print(f":::::: Beacon check")

        try:
            beacon_check()
        except Exception as ex:
            if verbose == 'True':
                print(f"   {dt_string} ERROR in BEACON check \n{ex}")

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
