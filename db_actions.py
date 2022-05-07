from sqlalchemy import create_engine, table, column
from configparser import ConfigParser
import os

watchdog = create_engine('sqlite:///watchdog.db')

folder = os.getcwd()# folder = os.path.dirname(os.path.realpath(__file__))

def secrets(filename=folder+'/secrets.txt', section='helium'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    secrets = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            secrets[param[0]] = param[1]
    else:
        raise Exception(f"[ERROR] Section {section} not found in the {filename} file")
    
    print(f"------| Current SECRETS {secrets}")
    return secrets
# secrets()

def get_last_ota():
    conn = watchdog.connect()
    query_list = conn.execute(f"SELECT value FROM hotspot WHERE attribute = 'ota' ORDER BY id desc LIMIT 1")
    content = query_list.cursor.fetchall()
    ota = content[0:1][0][0]
    conn.close()
    # print(f"------| Current OTA version is {ota}")
    
    return int(ota)
# get_last_ota()

def get_last_rewards():
    conn = watchdog.connect()
    query_list = conn.execute(f"SELECT value FROM hotspot WHERE attribute = 'rewards' ORDER BY id desc LIMIT 1")
    content = query_list.cursor.fetchall()
    rewards = content[0:1][0][0]
    conn.close()
    # print(f"------| Current Total rewards are {rewards} HNT")
    
    return round(float(rewards), 4)
# get_last_rewards()

def insert_ota(ota_new):
    new_version = False
    conn = watchdog.connect()
    query_list = conn.execute(f"SELECT value FROM hotspot WHERE attribute = 'ota' ORDER BY id desc LIMIT 1")
    content = query_list.cursor.fetchall()
    ota_last = content[0:1][0][0]
    # print(f"------| Current OTA version is {ota_last}")
    
    if int(ota_new) > ota_last:
        conn = watchdog.connect()
        add_ota = conn.execute(f"INSERT INTO hotspot(attribute, value) VALUES ('ota', {int(ota_new)})  ")
        conn.close()
        new_version = True
        # print(f"------| OTA version changed to {ota_new}")
    
    else:
        print(f"------| OTA version did not change ")
        
    return new_version
# insert_ota(99)


def insert_rewards(rewards_new):
    new_rewards = False
    conn = watchdog.connect()
    query_list = conn.execute(f"SELECT value FROM hotspot WHERE attribute = 'rewards' ORDER BY id desc LIMIT 1")
    content = query_list.cursor.fetchall()
    rewards_last = content[0:1][0][0]
    # print(f"------| Current Total rewards are {rewards_last} HNT")
    
    if float(rewards_new) > rewards_last:
        conn = watchdog.connect()
        add_ota = conn.execute(f"INSERT INTO hotspot(attribute, value) VALUES ('rewards', {float(rewards_new)})  ")
        conn.close()
        new_rewards = True
        # print(f"------| Total rewards changed to {rewards_new}")
    
    else:
        print(f"------| Total rewards did not change ")
        
    return new_rewards
