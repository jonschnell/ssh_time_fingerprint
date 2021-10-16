#jon schnell

import string
import argparse
import paramiko
from paramiko import SSHClient
import json
import time
import sys
import numpy as np


if __name__ == "__main__":
    #argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("IP", help="[IP] OR [FQDN] to be fingerprinted")
    parser.add_argument("uname", help="[uname] username to log in as")
    parser.add_argument("passwd", help="[passwd] password to log in with")
    parser.add_argument("port", help="[port] port to connect on")
    
    args = parser.parse_args()
    
    IP = args.IP
    passwd = args.passwd
    uname = args.uname
    port = args.port
    
    host = IP
    username = uname
    password = passwd
    command = "pwd"
    
    #print(IP)
    client = SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    #client.load_host_keys('/home/nemo/.ssh/known_hosts')
    #client.load_system_host_keys()
    #client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    timeARR = []

    for x in range(5):
        time.sleep(1)
        start = time.time()
        try:
            client.connect(host, port, username, password, look_for_keys=False, allow_agent=False)
        except:
            finish = time.time()
            #continue
        finish = time.time()
        total = finish - start
        timeARR.append(total)
        print(f'Time: {total}')
    average = np.average(timeARR)
    median = np.median(timeARR)
    std = np.std(timeARR)
    print(f'Average: {average}')
    print(f'Median: {median}')
    print(f'STD: {std}')

    #stdin, stdout, stderr = client.exec_command(command)
    #lines = stdout.readlines()
    #print(lines)
