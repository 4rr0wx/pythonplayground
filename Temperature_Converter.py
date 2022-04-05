## Temperature Converter
#einheit1: Einheit der ersten Temperatur
#einheit2: Einheit in die Umgerechnet werden soll
#temp1: Temperatur, welche umgerechnet werden soll
#temp2: umgerechnete Temperatur

print("Tempconverter V0.1 \n")
print("Mit diesem Programm kann man jede Temperatureinheit in jede andere Temperatureinheit umwandeln \n")
print("Bitte Starteinheit auswählen: \n 1: Celsius \n 2: Fahrenheit \n 3:Kelvin")

einheit1 = input("\n Einheit:") # Input Erste Einheit
print("Gewählte Einheit:", einheit1 )

einheit1 = float(einheit1)

while einheit1 < 0 or einheit1 > 3: #Falsche eingabe abfrage
    print("Falsche Auswahl! \n Bitte Wiederholen")
    einheit1 = input("\n Einheit:")
    print("Gewählte Einheit:", einheit1)
    einheit1 = float(einheit1)

temp1 = input("Bitte erste Temperatur in der gewählten Einheit eingeben:\n") #Temp1 eingabe
print("Eingegebene Temperatur:", temp1)



#Abfragen worauf umgerechnet werden soll
if einheit1 == 1: #Celsius
    einheit2 = input("Bitte 2. Einheit wählen:\n 1: Fahrenheit\n 2: Kelvin\n")
    einheit2 = float(einheit2)

    while einheit2 < 0 or einheit2 > 2: #Falsche eingabe abfrage
        print("Falsche Auswahl! \n Bitte Wiederholen")
        einheit2 = input("\n Einheit:")
        print("Gewählte Einheit:", einheit2)
        einheit2 = float(einheit2)
    
    if einheit2 == 1: #Fahrenheit
        temp2 = (1 °C × 9/5) + 32
    elif einheit2 == 2: #Kelvin


elif einheit1 == 2: #Fahrenheit
    einheit2 = input("Bitte 2. Einheit wählen:\n 1: Celsius\n 2: Kelvin\n")
    einheit2 = float(einheit2)

    while einheit2 < 0 or einheit2 > 2: #Falsche eingabe abfrage
        print("Falsche Auswahl! \n Bitte Wiederholen")
        einheit2 = input("\n Einheit:")
        print("Gewählte Einheit:", einheit2)
        einheit2 = float(einheit2)

elif einheit1 == 3: #Kelvin
    einheit2 = input("Bitte 2. Einheit wählen:\n 1: Fahrenheit\n 2: Celsius \n")
    einheit2 = float(einheit2)

    while einheit2 < 0 or einheit2 > 2: #Falsche eingabe abfrage
        print("Falsche Auswahl! \n Bitte Wiederholen")
        einheit2 = input("\n Einheit:")
        print("Gewählte Einheit:", einheit2)
        einheit2 = float(einheit2)
