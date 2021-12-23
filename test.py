import helium
import bobcat
import time

cache_name = 'alert_shadow_iguana'
cache_address = '11q2UB9Cy9GsdHkHCn2K1F2LZLxDSfe9Xa4F3ir1NMfTZZ6bs7R'
cache_ip = '192.168.1.4'
cache_ota_last = 0
cache_activity_count_last = 0


while True:
    gap = bobcat.bobcat_miner_status(cache_ip)
    block_gap =  gap['block_gap'] 
    print(block_gap)
    time.sleep(3)