import os
import datetime
import time

for a in range(1,256):
    
    print("Scan gestartet am: " + str(datetime.datetime.now())) #für den Scanzeitpunkt
    print("-------------------------------------------------") # für die Trennung
    print(f"[~] Scanne IP: {a}") #für die IP-Adresse
    
    ip = f"123.456.7.{a}" # Hier die IP-Adresse anpassen
    
    time.sleep(0) # für die Pause zwischen den Scans (in Sekunden)
    response = os.system(f"ping -n 1  {ip}") # für den Ping-Befehl (Windows linux ist "ping -c 1")
    
    if response == 0: # falls der Ping erfolgreich war
        print(f"[+] Gerät online {ip}") # dann wird die IP-Adresse ausgegeben mt dem string "Gerät online"
    
    else: 
        print(f"[-] Keine Antwort von: {ip} erhalten") # falls der Ping nicht erfolgreich war, wird die IP-Adresse ausgegeben mit dem string "Keine Antwort von: "
    print("-------------------------------------------------") # für die Trennung

    # coded by: Nico404