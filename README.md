# A wrapper around the BOBCAT 300 hotspot and HELIUM APIs in order to monitor the status and performance of the hotspot.


# Script <code>helium_watchdog.py</code> is checking :
- OTA version change
- Blockchain sync status
- Rewards change

# Configure your details and preferences in the "secrets.txt" file
- <b>cache_name</b>= your hotspot animal name like "alert_shadow_iguana"
- <b>cache_address</b>= your hotspot public blockchain address like "11q2UB9Cy9GsdHkHCn2K1F2LZLxDSfe9Xa4F3ir1NMfTZZ6bs7R"
- <b>cache_ip</b>= your internal local IP like "192.168.1.4"
- <b>sleep</b>= the number of seconds between checks like "7200"
- <b>send_emails</b>= flag it as "True" if you want to get emails when actions are taken / else "False"
- <b>email_to</b>= add your email address here 
- <b>log</b>= flag it as "True" if you want to write to a logfile when actions are taken / else "False"
- <b>verbose</b>= flag it as "True" if you want to see command line print outs when actions are taken / else "False"
- <b>dry_run</b>= use "True" if you want to just test the script by printing out what actions are taken without actually taking them / else "False"

# Install the needed libraries from the requirements.txt file
<code>pip3 install requirements.txt</code>

# Make a dry run
- Change the "dry_run" value to "True" in secrets.txt
- Maybe also change the "sleep" value to "600" so you don't need to wait too much
- Run the script 
<code>python3 helium_watchdog.py</code>

# If all went ok then deploy !
- Change the "dry_run" value to "False" in secrets.txt
- Change the "sleep" value to minimum "3600" (1 hour) but suggested is "7200" (2 hours)
- Run the script 
<code>python3 helium_watchdog.py</code>

---

# Script <code>helium_watchdog_reboot_schedule.py</code> is :
- just rebooting at a regular time interval

# Configure your details and preferences in the "secrets.txt" file
- <b>cache_name</b>= your hotspot animal name like "alert_shadow_iguana"
- <b>cache_address</b>= your hotspot public blockchain address like "11q2UB9Cy9GsdHkHCn2K1F2LZLxDSfe9Xa4F3ir1NMfTZZ6bs7R"
- <b>cache_ip</b>= your internal local IP like "192.168.1.4"
- <b>sleep</b>= the number of seconds between checks like "7200"
- <b>verbose</b>= flag it as "True" if you want to see command line print outs when actions are taken / else "False"
- <b>dry_run</b>= use "True" if you want to just test the script by printing out what actions are taken without actually taking them / else "False"

# Install the needed libraries from the requirements.txt file
<code>pip3 install requirements.txt</code>

# Make a dry run
- Change the "dry_run" value to "True" in secrets.txt
- Maybe also change the "sleep" value to "600" so you don't need to wait too much
- Run the script 
<code>python3 helium_watchdog_reboot_schedule.py</code>

# If all went ok then deploy !
- Change the "dry_run" value to "False" in secrets.txt
- Change the "sleep" value to minimum "3600" (1 hour) but suggested is "7200" (2 hours)
- Run the script 
<code>python3 helium_watchdog_reboot_schedule.py</code>

---
# Please Donate if this is helpful
<code>1399umgdrqkxgNjJsXaaW2xqJtHNXPP5dYKqH7miu7ap83JYTmy</code>

# Looking for owners of hotspots from other manufacturers to extend the functionalities !!!
