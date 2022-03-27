from functools import cache
import bobcat
import helium
import _gmail
from utilities import LogFile

import time
from datetime import datetime

from sqlalchemy import create_engine, table, column
import db_actions
import secrets

secrets = db_actions.secrets()

verbose = secrets['verbose']
send_emails = secrets['send_emails']
dry_run = secrets['dry_run']
cache_name = secrets['cache_name']
log = secrets['log']
email_to = secrets['email_to']
sleep = int(secrets['sleep'])
# print(verbose)

def initialize():
    ota_current = int(bobcat.bobcat_ota(secrets['cache_ip'])['ota_version_min'])
    db_actions.insert_ota(ota_current)
    
    rewards = helium.get_hotspot_all_time_rewards(secrets['cache_address'])['hnt_rewards_total']
    # print(rewards)
    db_actions.insert_rewards(rewards)

# Check for OTA version updates
def ota_check(ip=secrets['cache_ip']):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    cache_ota_last = db_actions.get_last_ota()
    ota = bobcat.bobcat_ota(ip)
    ota_current = ota['ota_version_min']
    
    if verbose == 'True':
        print(f"   {dt_string} OTA version currently read is {ota_current}")
        
    if ota['status_code'] == 200:
        db_actions.insert_ota(ota_current)
        if int(ota_current) > cache_ota_last and cache_ota_last != 0: # v1.1 fix to avoid reboot when starting the script for the 1st time as the new OTA will always be higher than 0
            if dry_run == 'False':
                if verbose == 'True':
                    print(f"   {dt_string} OTA version increased (v{ota_current}) >>>>> REBOOTING <<<<<")
                bobcat.bobcat_reboot(ip)
                time.sleep(30)
            else:
                if verbose == 'True':
                    print(f"   {dt_string} OTA version increased (v{ota_current}) >>>>> DRY -- REBOOTING <<<<<")
            if send_emails == 'True':
                _gmail.send_email("OTA version increased", f"""{dt_string}\n{cache_name}\nOTA version increased (v{ota_current}) \n>>>>> REBOOTING <<<<<""", email_to)
                if verbose == 'True':
                    print(f"   {dt_string} Sending email ...")
            
    else:
        if verbose == 'True':
            print(f"   {dt_string} Bobcat hotspot (ota) API not responding")

# ota_check()

# Check for stale hotspot
def stale_check(address = secrets['cache_address'], ip=secrets['cache_ip']):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    cache_last_rewards = db_actions.get_last_rewards()
    
    rewards = helium.get_hotspot_all_time_rewards(secrets['cache_address'])
    rewards_value = rewards['hnt_rewards_total']
    if rewards['status_code'] == 200:
        # print(activity_count)
        if float(rewards_value) > float(cache_last_rewards) and float(cache_last_rewards) != 0: # v1.1 fix to avoid reboot when starting the script for the 1st time as the new rewards value will always be higher than 0
            # Do nothing   
            db_actions.insert_rewards(rewards_value)
            if verbose == 'True':
                print(f"   {dt_string} Updated Rewards to : {rewards_value}")
            
        else:
            if dry_run == 'False':
                if verbose == 'True':
                    print(f"   {dt_string} Hotspot is STALE (0 additional rewards since last check) >>>>> REBOOTING <<<<<")
                bobcat.bobcat_reboot(ip)
                time.sleep(30)
            else:
                if verbose == 'True':
                    print(f"   {dt_string} Hotspot is STALE (0 additional rewards since last check) >>>>> DRY -- REBOOTING <<<<<")
            
            if send_emails == 'True':
                _gmail.send_email("Hotspot is STALE", f"""{dt_string}\n{cache_name}\nHotspot is STALE (0 additional rewards since last check) \n>>>>> REBOOTING <<<<<""", email_to)
                if verbose == 'True':
                    print(f"   {dt_string} Sending email ...")
    else:
        if verbose == 'True':
            print(f"   {dt_string} Helium API not responding")
# stale_check()

# Check for out of sync
def sync_check(ip=secrets['cache_ip']):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    block = bobcat.bobcat_miner_status(ip)
    block_gap = block['block_gap']
    if block_gap == '-':
        time.sleep(300)
    block_gap = int(block['block_gap'])
    if block['status_code'] == 200:
        
        if block_gap < 400 and block_gap > -1:
            # Do nothing   
            if verbose == 'True': 
                print(f"   {dt_string} Current block gap is {block_gap}")
            pass
        elif block_gap < -60:
            if verbose == 'True': 
                print(f"   {dt_string} Blockchain is slow (gap = {block_gap}), nothing can be done...")
            if send_emails == 'True':
                _gmail.send_email("Blockchain is slow", f"""{dt_string}\n{cache_name}\nBlockchain is slow (gap = {block_gap}) \nNothing can be done...""", email_to)  
                if verbose == 'True':
                    print(f"   {dt_string} Sending email ...")
        elif block_gap < 100 and block_gap > 30:
            if verbose == 'True': 
                print(f"   {dt_string} Hotspot is slightly out of sync (gap = {block_gap}), nothing that can be done...")
            # Fast Sync <<<<<>>>>>
            if send_emails == 'True':
                _gmail.send_email("Hotspot is OUT OF SYNC", f"""{dt_string}\n{cache_name}\nHotspot is slightly OUT OF SYNC (gap = {block_gap}) \nCan't yet use fast sync ... need to wait for 400 blocks gap.""", email_to)  
                if verbose == 'True':
                    print(f"   {dt_string} Sending email ...")
        elif block_gap > 400:
            if dry_run == 'False':
                if verbose == 'True':
                    print(f"   {dt_string} Hotspot is OUT OF SYNC (gap = {block_gap}) >>>>> FAST SYNC <<<<<")
                bbobcat.bobcat_fast_sync(ip)
                time.sleep(30)
            else:
                if verbose == 'True':
                    print(f"   {dt_string} Hotspot is OUT OF SYNC (gap = {block_gap}) >>>>> DRY -- FAST SYNC <<<<<")
            
            
            if send_emails == 'True':
                _gmail.send_email("Hotspot is OUT OF SYNC", f"""{dt_string}\n{cache_name}\nHotspot is OUT OF SYNC (gap = {block_gap}) \n>>>>> FAST SYNC <<<<<""", email_to)  
                if verbose == 'True':
                    print(f"   {dt_string} Sending email ...")      
    else:
        if verbose == True:
            print(f"   {dt_string} Bobcat hotspot (sync) API not responding")
# sync_check()
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
            print(f":::::: SYNC hotspot check")

        try:
            sync_check()     
        except Exception as ex:
            if verbose == 'True':
                print(f"   {dt_string} ERROR in SYNC status check \n{ex}")
        
        #####
        if verbose == 'True':
            print(f":::::: OTA version check")

        try:
            ota_check()       
        except Exception as ex:
            if verbose == 'True':
                print(f"   {dt_string} ERROR in OTA version check \n{ex}")

            
        #####
        if verbose == 'True':
            print(f":::::: STALE hotspot check")

        try:
            stale_check()
        except Exception as ex:
            if verbose == 'True':
                print(f"   {dt_string} ERROR in STALE check \n{ex}")
        

        #####
        
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
