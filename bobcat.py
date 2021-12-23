import requests
import time
from datetime import datetime
import requests

####################
# BOBCAT           #
####################

def bobcat_temp(ip):
    # api-endpoint
    URL = f"http://{ip}/temp.json"

    # sending get request and saving the response as response object
    r = requests.get(url = URL)

    # extracting data in json format
    data = r.json()
    # extracting latitude, longitude and formatted address 

    # of the first matching location
    timestamp = data['timestamp']
    temp_avg = ( int(data['temp0']) + int(data['temp1']) ) / 2

    # printing the output
    # print(f"-----------------------------------------------")
    # print(f"Time                      : {timestamp}")
    # print(f"BOBCAT miner temperature  : {temp_avg} Celsius")

    return {"time":'{timestamp}', "temp":{temp_avg}}


def bobcat_miner_status(ip):
    # api-endpoint
    URL = f"http://{ip}/status.json"
    status = ""
    block_gap = 0
    status_code = 0

    try:
        # sending get request and saving the response as response object
        r = requests.get(url = URL)
        status_code = r.status_code
        
        # extracting data in json format
        data = r.json()

        # of the first matching location
        status = data['status']
        block_gap = data['gap']
        
        # printing the output
        # print(f"-----------------------------------------------")
        # print(f"Miner Status              : {status}")
        # print(f"BlockChain Gap            : {block_gap} blocks")
        
        return {"status":'status', "block_gap":block_gap, "status_code":status_code}

    except:
        return {"status":'status', "block_gap":block_gap, "status_code":status_code}

    



def bobcat_ota(ip):

    # api-endpoint
    URL = f"http://{ip}/miner.json"
    ota_version_full = 0
    ota_version_min = 0
    status_code = 0

    try:

        # sending get request and saving the response as response object
        r = requests.get(url = URL)
        status_code = r.status_code
        
        # extracting data in json format
        data = r.json()
    
        # extracting latitude, longitude and formatted address 
        # of the first matching location
        ota_version_full = data['ota_version']

        
        if ota_version_full is not None:
            ota_version_min = ota_version_full[6:]

        # printing the output
        # print(f"-----------------------------------------------")
        # print(f"OTA version               : {ota_version_full}")
        # print(f"OTA version               : {ota_version_min}")
        
        return {"ota_version_full":f'{ota_version_full}', "ota_version_min":ota_version_min, "status_code":status_code}

    except:
        return {"ota_version_full":f'{ota_version_full}', "ota_version_min":ota_version_min, "status_code":status_code}



def bobcat_reboot(ip):

    # api-endpoint
    URL = f"http://{ip}/admin/reboot"
    HEADERS = {'Authorization': 'Basic Ym9iY2F0Om1pbmVy'}

    r = requests.post(URL, headers=HEADERS)
    return {"response":f'{r}'}





def bobcat_fast_sync(ip):
    # api-endpoint
    URL = f"http://{ip}/admin/fastsync"
    HEADERS = {'Authorization': 'Basic Ym9iY2F0Om1pbmVy'}

    r = requests.post(URL, headers=HEADERS)

    return {"response":f'{r}'}

if __name__ == "__main__":
    ip = "192.168.1.4"
    bobcat_temp(ip)
    bobcat_miner_status(ip)
    bobcat_ota(ip)
    
    bobcat_fast_sync()
    bobcat_reboot()