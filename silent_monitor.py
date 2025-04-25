import os
import datetime
import time

for a in range(1,11):
    
    print("Scan gestartet am: " + str(datetime.datetime.now()))
    print("-------------------------------------------------")
    print(f"[~] Scanne IP: {a}")
    ip = f"192.168.1.{a}"
    
    time.sleep(2)
    response = os.system(f"ping -n 1  {ip}")
    
    if response == 0:
        print(f"[+] Gerät online {ip}")
    
    else: 
        print(f"[-] Keine Antwort von: {ip} erhalten")