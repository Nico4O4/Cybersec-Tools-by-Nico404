import socket #zum verbinden mit dem Ziel
import datetime #für den Scanzeitpunkt


found_ports_open = [] # Liste für die offenen Ports

def scanned_ports():
    return found_ports_open # gibt die Liste der offenen Ports zurück

print("""
   ____        _      __      ____             __                                          
  / __ \__  __(_)____/ /__   / __ \____  _____/ /_                                         
 / / / / / / / / ___/ //_/  / /_/ / __ \/ ___/ __/                                         
/ /_/ / /_/ / / /__/ ,<    / ____/ /_/ / /  / /_                                           
\___\_\__,_/_/\___/_/|_|  /_/__  \____/_/   \__/   _   ________________  __ __  ____  __ __
  _________  ____/ /__  ____/ /  / /_  __  ___    / | / /  _/ ____/ __ \/ // / / __ \/ // /
 / ___/ __ \/ __  / _ \/ __  /  / __ \/ / / (_)  /  |/ // // /   / / / / // /_/ / / / // /_
/ /__/ /_/ / /_/ /  __/ /_/ /  / /_/ / /_/ /    / /|  // // /___/ /_/ /__  __/ /_/ /__  __/
\___/\____/\__,_/\___/\__,_/  /_.___/\__, (_)  /_/ |_/___/\____/\____/  /_/  \____/  /_/   
                                    /____/                                                """) # ASCII Art für den Portscanner

ziel = input("Gib die IP-Adresse ein: ")# Hier die IP-Adresse anpassen
print("-------------------------------------------------") # für die Trennung

for port in range(0, 11):  # die anzahl der Ports die gescannt werden sollen, maximal 65535, hier 10 für den Test
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# AF_INET für IPv4 und SOCK_STREAM für TCP 
                            
    s.settimeout(0.1)  # damit es nicht ewig hängt wenn es nichts findet
    
    ergebnis = s.connect_ex((ziel, port)) # connect_ex gibt 0 zurück, wenn der Port offen ist, sonst endet das Programm mit einer Fehlermeldung
    
    if ergebnis == 0: # 0 bedeutet, dass der Port offen ist weil connect_ex immer 0 zurückgibt wenn der Port offen ist
        print(f"Port {port} ist offen!") # wenn der Port offen ist, wird die Portnummer ausgegeben mit dem string "Port ist offen!" 
        found_ports_open.append(port) # wenn der Port offen ist, wird die Portnummer in die Liste "found_ports_open" hinzugefüg    
   
    s.close() # am ende wird die Verbindung geschlossen

print("-------------------------------------------------") # für die Trennung damit es schöner aussieht

time = datetime.datetime.now() # für den Scanzeitpunkt am ende 
print("Scan beendet am: " + str(time)) # printet den Scanzeitpunkt aus


print("Offene gefundene Ports: " + str(found_ports_open)) # printet die offenen Ports aus

print("-------------------------------------------------") # für die Trennung

# coded by: Nico404