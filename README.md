###### This is a wrapper around the BOBCAT 300 hotspot and HELIUM APIs in order to monitor the status and performance of the hotspot.

#### 1. Copy the full repository to your device

#### 2. Open a terminal window depending on your operating system and Move to the directory on your device
<code>cd your_path/helium_watchdog</code>

#### 3. Script <code>helium_watchdog.py</code> is checking :
- OTA version change
- Blockchain sync status
- Rewards change

#### 4. Configure your details and preferences in the "secrets.txt" file
- <code>cache_name</code>= your hotspot animal name like "alert_shadow_iguana"
- <code>cache_address</code>= your hotspot public blockchain address like "11q2UB9Cy9GsdHkHCn2K1F2LZLxDSfe9Xa4F3ir1NMfTZZ6bs7R"
- <code>cache_ip</code>= your internal local IP like "192.168.1.4"
- <code>sleep</code>= the number of seconds between checks like "7200"
- <code>send_emails</code>= flag it as "True" if you want to get emails when actions are taken / else "False"
- <code>send_telegram_msg</code>= flag it as "True" if you want to get messages when actions are taken / else "False"
- <code>email_to</code>= add your email address here 
- <code>tg_token</code>= api key of the telegram bot
- <code>msg_to</code>= your telegram user id, find out yours with @userinfobot
- <code>log</code>= flag it as "True" if you want to write to a logfile when actions are taken / else "False"
- <code>verbose</code>= flag it as "True" if you want to see command line print outs when actions are taken / else "False"
- <code>dry_run</code>= use "True" if you want to just test the script by printing out what actions are taken without actually taking them / else "False"

#### 5. Install the needed libraries from the requirements.txt file
<code>pip3 install -r requirements.txt</code>

#### 6. Make a dry run
- Change the "dry_run" value to "True" in secrets.txt
- Maybe also change the "sleep" value to "600" so you don't need to wait too much
- Run the script 
<code>python3 helium_watchdog.py</code>

#### 7. If all went ok then deploy !
- Change the "dry_run" value to "False" in secrets.txt
- Change the "sleep" value to minimum "3600" (1 hour) but suggested is "7200" (2 hours)
- Run the script 
<code>python3 helium_watchdog.py</code>

---

#### 8. (variant) Script <code>helium_watchdog_reboot_schedule.py</code> is :
- just rebooting at a regular time interval

#### 9. (variant) Configure your details and preferences in the "secrets.txt" file
- <b>cache_name</b>= your hotspot animal name like "alert_shadow_iguana"
- <b>cache_address</b>= your hotspot public blockchain address like "11q2UB9Cy9GsdHkHCn2K1F2LZLxDSfe9Xa4F3ir1NMfTZZ6bs7R"
- <b>cache_ip</b>= your internal local IP like "192.168.1.4"
- <b>sleep</b>= the number of seconds between checks like "7200"
- <b>verbose</b>= flag it as "True" if you want to see command line print outs when actions are taken / else "False"
- <b>dry_run</b>= use "True" if you want to just test the script by printing out what actions are taken without actually taking them / else "False"

#### 10. (variant) Install the needed libraries from the requirements.txt file
<code>pip3 install requirements.txt</code>

#### 11. (variant) Make a dry run
- Change the <code>dry_run</code> value to "True" in secrets.txt
- Maybe also change the <code>sleep</code> value to "600" so you don't need to wait too much
- Run the script 
<code>python3 helium_watchdog_reboot_schedule.py</code>

#### 12. (variant)  If all went ok then deploy !
- Change the "dry_run" value to "False" in secrets.txt
- Change the "sleep" value to minimum "3600" (1 hour) but suggested is "7200" (2 hours)
- Run the script 
<code>python3 helium_watchdog_reboot_schedule.py</code>

---
## Please Donate if this is helpful
<code>1399umgdrqkxgNjJsXaaW2xqJtHNXPP5dYKqH7miu7ap83JYTmy</code>

## Looking for owners of hotspots from other manufacturers to extend the functionalities !!!
