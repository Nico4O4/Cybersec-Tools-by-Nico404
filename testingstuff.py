#zum austesten random zeug in python lol
import msvcrt # für die Tasteneingabe


name = input("Bitte gib deinen Namen ein: ") # hier wird der Name eingegeben

ausgabe = (f"Hallo {name} wie geht es dir heute?")

zusatz = (f"Ausserdem, wilkommen zurück in der Python Welt {name}!")

print(ausgabe)
print(zusatz)



print("Drücke 1 um das Programm zu beenden") # hier wird die Taste '1' angezeigt

while True: # anfang der Schleife
    
    if msvcrt.kbhit(): # das ist eine Funktion die überprüft ob eine Taste gedrückt wurde
        close = msvcrt.getch() # hier wird die Taste '1' abgefragt 
        
        try: # einfach gesagt ist try eine Funktion die versucht etwas auszuführen und wenn ein Fehler auftritt wird die except Funktion ausgeführt 
            close = close.decode()  # Jetzt ist close ein String, z.B. '1'
        
        except: # except ist eine funktion die ausgeführt wird wenn ein Fehler auftritt man kann selber entscheiden was passieren soll also except heisst ja auch in englisch "ausser" also wenn ein Fehler auftritt wird die Funktion ausgeführt
            
            print("Falsche Eingabe, bitte drücke '1' um das Programm zu beenden.") # Wenn die Eingabe nicht dekodiert werden kann, wird eine Fehlermeldung ausgegeben
            
            continue # Wenn die Eingabe nicht dekodiert werden kann, wird die Schleife fortgesetzt
        
        if close == '1':  # Jetzt richtiger Vergleich als String
            print("Auf Wiedersehen!")
            break  # Programm beende