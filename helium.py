import requests
import time
from datetime import datetime


####################
# HELIUM           #
####################
def get_hotspot_details(address):
    # api-endpoint
    URL = f"https://api.helium.io/v1/hotspots/{address}"
    
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    
    # extracting data in json format
    data = r.json()
    # print(data)
    
    # extracting latitude, longitude and formatted address 
    # of the first matching location
    timestamp = data['data']['status']['timestamp']
    status = data['data']['status']['online']
    ip_address = data['data']['status']['listen_addrs'][0]
    reward_scale = data['data']['reward_scale']
    animal_name = data['data']['name']
    address = data['data']['address']
    
    print(f"ANIMAL name               : {animal_name}")
    print(f"Timestamp                 : {timestamp}")
    print(f"Status                    : {status}")
    print(f"Last IP address           : {ip_address}")
    print(f"Reward scale              : {round(reward_scale,2)}")
    print(f"HNT address               : {address}")
    return {"ip_address":ip_address}
       

def get_hotspot_activity_count(address):
    # api-endpoint
    URL = f"https://api.helium.io/v1/hotspots/{address}/activity/count"
    poc_receipts = 0
    poc_requests = 0
    rewards = 0
    status_code = 0
    
    try:
        # sending get request and saving the response as response object
        r = requests.get(url = URL)
        status_code = r.status_code
        
        # extracting data in json format
        data = r.json()
        # print(data)

        poc_receipts = data['data']['poc_receipts_v1']
        poc_requests = data['data']['poc_request_v1']
        rewards = data['data']['rewards_v2']
        
        # print(f"POC receipts count        : {poc_receipts}")
        # print(f"POC requests count        : {poc_requests}")
        # print(f"Rewards count             : {rewards}")
        
        return {"poc_receipts":poc_receipts, "poc_requests":poc_requests, "rewards":rewards, "status_code":status_code}
    except:
        return {"poc_receipts":poc_receipts, "poc_requests":poc_requests, "rewards":rewards, "status_code":status_code}
        
#get_hotspot_activity_count('11q2UB9Cy9GsdHkHCn2K1F2LZLxDSfe9Xa4F3ir1NMfTZZ6bs7R')


def get_hotspot_all_time_rewards(address):
    from datetime import date, timedelta
    today = date.today()
    tomorrow = today + timedelta(days=1)
    inception = '2021-10-01'
    hnt_rewards_total = 0
    status_code = 0
    
    try:
        # api-endpoint
        URL = f"https://api.helium.io/v1/hotspots/{address}/rewards/sum?min_time={inception}&max_time={tomorrow}"
        
        # sending get request and saving the response as response object
        r = requests.get(url = URL)
        status_code = r.status_code
        
        # extracting data in json format
        data = r.json()
        # print(data)
        
        hnt_rewards_total = round(data['data']['total'], 4)
        return {"hnt_rewards_total":hnt_rewards_total,"status_code":status_code}
    except:
        return {"hnt_rewards_total":hnt_rewards_total,"status_code":status_code}   

def get_hotspot_rewards(address):
    from datetime import date, timedelta
    today = date.today()
    tomorrow = today + timedelta(days=1)
    yesterday = today - timedelta(days=1)
    seven_days_ago = today - timedelta(days=7)
    inception = '2021-10-01'
    
    # api-endpoint
    URL = f"https://api.helium.io/v1/hotspots/{address}/rewards/sum?min_time=2021-10-25&max_time={tomorrow}"
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    
    # extracting data in json format
    data = r.json()
    # print(data)
    
    hnt_rewards_total = round(data['data']['total'], 2)
    print(f"TOTAL REWARDS ============= {hnt_rewards_total}")
    
    #######################
    # api-endpoint
    URL = f"https://api.helium.io/v1/hotspots/{address}/rewards/sum?min_time={seven_days_ago}&max_time={tomorrow}"
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    
    # extracting data in json format
    data = r.json()
    # print(data)
    
    hnt_rewards_seven_days = round(data['data']['total'], 2)
    print(f"REWARDS Last 7 days       : {hnt_rewards_seven_days}")
    print(f"REWARDS AVG 7 days        : {hnt_rewards_seven_days/7}")
        
    #######################
    # api-endpoint
    URL = f"https://api.helium.io/v1/hotspots/{address}/rewards/sum?min_time={yesterday}&max_time={today}"
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    
    # extracting data in json format
    data = r.json()
    # print(data)
    
    hnt_rewards_yesterday = round(data['data']['total'], 2)
    print(f"REWARDS Yesterday         : {hnt_rewards_yesterday}")
       
    
    #######################
    # api-endpoint
    URL = f"https://api.helium.io/v1/hotspots/{address}/rewards/sum?min_time={today}&max_time={tomorrow}"
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    
    # extracting data in json format
    data = r.json()
    # print(data)
    
    hnt_rewards_today = round(data['data']['total'], 2)
    print(f"REWARDS TODAY             : {hnt_rewards_today}")
    
# !!!!!!
def get_hotspot_rewards_list(address):
    from datetime import date, timedelta
    today = date.today()
    tomorrow = today + timedelta(days=1)
    yesterday = today - timedelta(days=1)
    seven_days_ago = today - timedelta(days=7)
    
    # api-endpoint
    URL = f"https://api.helium.io/v1/hotspots/{address}/rewards?min_time={today}&max_time={tomorrow}"
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    
    # extracting data in json format
    raw = r.json()
    empty = False
    if raw["data"] == []:
        empty = True
        
    count_today = len(raw['data'])
    
    if empty == True:
        cursor = raw["cursor"]
        URL_new = f"https://api.helium.io/v1/hotspots/{address}/rewards?min_time={today}&max_time={tomorrow}&cursor={cursor}"
        # sending get request and saving the response as response object
        r = requests.get(url = URL_new)
        data = r.json()
        count_today = len(data['data'])
    
    ##############################
     # api-endpoint
    URL = f"https://api.helium.io/v1/hotspots/{address}/rewards?min_time={yesterday}&max_time={today}"
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    
    # extracting data in json format
    raw2 = r.json()
    empty2 = False
    if raw["data"] == []:
        empty2 = True
    
    count_yesterday = len(raw2['data'])
    if empty2 == True:
        cursor = raw2["cursor"]
        URL_new = f"https://api.helium.io/v1/hotspots/{address}/rewards?min_time={yesterday}&max_time={today}&cursor={cursor}"
        # sending get request and saving the response as response object
        r = requests.get(url = URL_new)
        data = r.json()
        count_yesterday = len(data['data'])
        
    print(f"Count of rewards TODAY     : {count_today}")
    print(f"Count of rewards YESTERDAY : {count_yesterday}")


def get_hotspot_witnessed_count(address):
    # api-endpoint
    URL = f"https://api.helium.io/v1/hotspots/{address}/witnessed"
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    
    # extracting data in json format
    data = r.json()
    witnessed_count = len(data['data'])
    print(f"Witnessed in last 5 days  : {witnessed_count}")
    
    
def get_hotspot_witnesses_count(address):
    # api-endpoint
    URL = f"https://api.helium.io/v1/hotspots/{address}/witnesses"
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    
    # extracting data in json format
    data = r.json()
    witnesses_count = len(data['data'])
    print(f"Witnesses in last 5 days  : {witnesses_count}")
      
    
def get_hotspot_challenges_count(address):
    # api-endpoint
    URL = f"https://api.helium.io/v1/hotspots/{address}/challenges"
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    
    # extracting data in json format
    data = r.json()
    challenges_count = len(data['data'])
    print(f"Challenges in last 5 days : {challenges_count}")

