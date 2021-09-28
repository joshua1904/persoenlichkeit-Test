import csv
import webbrowser

file = open('ExelMappe1.CSV', newline='')

fragen_csv = csv.DictReader(file,delimiter= ';')

# Definiert die Fragen reihe frage= string der rest int con 0 - 8
class Fragen():
    def __init__(self, frage, spalte1, spalte2, umgekehrteSpalte):
        self.frage = frage
        self.persönlichkeitsSpalte1 = spalte1
        self.persönlichkeitsSpalte2 = spalte2
        self.umgekehrtePersönlichkeitsSpalte = umgekehrteSpalte

fragenFeld = [Fragen("Das Leben gelingt, besser wenn man das Positive sieht, anstatt sich am Negativen aufzuhalten",6,-1,-1)]

#die fragenFeld Liste wird mit der csv Datei aufgefüllt
for item in fragen_csv:
   fragenFeld.append(Fragen(item['Frage'], int(item['spalte1']), int(item['spalte2']), int(item['umgekehrt'])))

rechnerListe = [0, 0, 0, 0, 0, 0, 0, 0,0]

#Testet ob die eingabe eine zahl zwischen 0 und 6 ist und gibt wenn das zu trifft true wenn nicht false aus
def richtigeEingabeTest(eingabe):
    if eingabe.isnumeric():
        if int(eingabe) <= 6 and int(eingabe) >= 0:
            return True
        else:
            return False
    else:
        return False

def fragenWertUmkehren(eingabe):
    zahl = int(eingabe)
    if zahl == 0:
        return 6
    elif zahl== 1:
        return 5
    elif zahl == 2:
        return 4
    elif zahl == 3:
        return 3
    elif zahl == 4:
        return 2
    elif zahl == 5:
        return 1
    elif zahl == 6:
        return 0

def persönlichkeitSpalteHinzufuegen(eingabe, spalte):
    if(spalte != -1):
        rechnerListe[spalte] += int(eingabe)
def umgekehrtePersönlichkeitHinzufuegen(eingabe, spalte):
    if(spalte != -1):
        rechnerListe[spalte] += fragenWertUmkehren(int(eingabe))
#Start Text für den User
print("Persönlichkeits Test")
print("Beantworte die Fragen mit den Zahlen 0 - 6")
print("Dabei seteht 0 für \"Trifft überhaupt nicht zu\" und 6 für \"Trifft voll und ganz zu\"")
print("Bitte versuche die 3(\"Neutral\") zu vermeiden")
print("Los Gehts: ")

#geht alle Fragen durch und addirt die Werte in der rechner Liste
for i in range(0,len(fragenFeld)):
    while True:
        print(i+1,") ",fragenFeld[i].frage)
        eingabe = input(">> ")
        if(richtigeEingabeTest(eingabe)):

           persönlichkeitSpalteHinzufuegen(eingabe, fragenFeld[i].persönlichkeitsSpalte1)
           persönlichkeitSpalteHinzufuegen(eingabe, fragenFeld[i].persönlichkeitsSpalte2)
           umgekehrtePersönlichkeitHinzufuegen(eingabe, fragenFeld[i].umgekehrtePersönlichkeitsSpalte)
           print(rechnerListe)
           break

print("Ergebnis: ")

for i in range(0,len(rechnerListe)):
    print("Persönlichkeit ",i+1," Wert: ",rechnerListe[i])

print("Um so höher die Zahlen der Persönlichkeits Typen sind, desto eher passt deine Persönöichkeit zu diesem Typen")

groeßterWert = 0
groeßterWertIndex = 0

# gibt den PersönlichkeitsTyp mit der hoechsten uebereinstimmung zurueck
for i in range(0,len(rechnerListe)):

    if(rechnerListe[i] > groeßterWert):
        groeßterWert = rechnerListe[i]
        groeßterWertIndex = i+1

print("Hoechste Wahrscheinlichkeit: Typ: ",groeßterWertIndex)

input("Drücke Enter um dir die Persönlichkeits Typen anzuschauen")
#oeffnet die pdf datei mit den Beschreibungen der Persönlichkeits Typen
webbrowser.open_new(r'file://C:\Users\joshu\PycharmProjects\PersönlichkeitsTest\Enneagramm Kurzbeschreibung-gedreht.pdf')
input("Drücke Enter um das Programm zu Beenden")



