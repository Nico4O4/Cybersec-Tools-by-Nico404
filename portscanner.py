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

while True: # Schleife für den IP Adressen Check ob es eine gültige IP ist und nnicht abc123
    print("-------------------------------------------------") # für die Trennung    
    ziel = input("Gib die IP-Adresse ein: ")# Hier die IP-Adresse anpassen
    print("-------------------------------------------------") # für die Trennung
    
    try: 
        socket.gethostbyname(ziel)
    except socket.gaierror:
        print("Ungültige Eingabe. Bitte Gültige IP-Adresse oder Domain angeben.")
        continue # die Schleife startet neu weil keine gültige IP / Domain

    # ---------------------------------------------------
    # while True: # Endlosschleife für den Portscanner # BÖSE!!!! (und unnötig ^^)
    # sobald 'ne gültige IP eingegeben wird, startet die für immer. (Danke für dein Kommentar und deine Hilfe :D)
    # ---------------------------------------------------

    for port in range(0, 11):  # die anzahl der Ports die gescannt werden sollen, maximal 65535, hier 10 für den Test
    

        netz = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# AF_INET für IPv4 (OSI Layer 3) und SOCK_STREAM für (OSI Layer 4) TCP / Variable "Netz" speichert die information zur Verbindung zum Beispiel bei welchen Port einen Verbindung möglich ist = offen
                        
        netz.settimeout(0.1)  # damit es nicht ewig hängt wenn es nichts findet oder es sonst einen fehler gibt
    
        ergebnis = netz.connect_ex((ziel, port)) # connect_ex gibt 0 zurück, wenn der Port offen ist, sonst endet das Programm mit einer Fehlermeldung / connect_ex macht einen Verbindungs versuch zu einem TCP Port -> er testet ob eine verbindung möglich ist  
        # Ergebnis speichert die Rückgabe von netz.connect_ex(), und das if fragt dann, ob ergebnis == 0 (also die Verbindung erfolgreich war) und entscheidet daraufhin, was im if-Block passiert.
    

    if ergebnis == 0: # 0 bedeutet, dass der Port offen ist weil connect_ex immer 0 zurückgibt wenn der Port offen ist
        print(f"Port {port} ist offen!") # wenn der Port offen ist, wird die Portnummer ausgegeben mit dem string "Port ist offen!" 
        found_ports_open.append(port) # wenn der Port offen ist, wird die Portnummer in die Liste "found_ports_open" hinzugefüg    

        netz.close() # am ende wird die Verbindung geschlossen 

    print("-------------------------------------------------") # für die Trennung damit es schöner aussieht

    time = datetime.datetime.now() # für den Scanzeitpunkt am ende 
    print("Scan beendet am: " + str(time)) # printet den Scanzeitpunkt aus


    print("Offene gefundene Ports: " + str(found_ports_open)) # printet die offenen Ports aus

    print("-------------------------------------------------") # für die Trennung

    while True: # Endlosschleife für das End-Menü
        menu = input("'Q' = Neue IP Adresse | 'E' = Beenden  ").strip().upper() # Menü für den Portscanner / # strip upper dient dazu das man auch kleine Buchstaben eingeben kann wie q oder e
    
        if menu == "E": # wenn man "E"eingibt wird das Programm beendet
            print("beendet ")
            exit()

        if menu == "Q": # wenn man "Q" eingibt kehrt man zur 1. Schleife zurück  (1 von 2 Schleifen)
            break

        else:
            print("Ungültige Eingabe")

# coded by: Nico404

# AUFGABEN:

# 1. Ipv6 support
# UDP support ertsmal gestrichen