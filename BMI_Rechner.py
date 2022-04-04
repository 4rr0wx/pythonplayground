
zeile1 = "              Kategorie | BMI (kg/m^2) \n" #Tabelle wird in Variablen eingespeichert
zeile2 = "         --------------|---------- \n"
zeile3 = "  Starkes Untergewicht | < 16 \n"
zeile4 = "Maessiges Untergewicht | 16-17 \n"
zeile5 = " Leichtes Untergewicht | 17-18,5 \n"
zeile6 = "         Normalgewicht | 18,5-25 \n"
zeile7 = "        Praeadipositas | 25-30 \n"
zeile8 = "     Adipositas Grad I | 30-35 \n"
zeile9 = "    Adipositas Grad II | 35-40 \n"
zeile10 = "   Adipositas Grad III | >= 40 \n"


print("Willkommen beim BMI-Rechner \n")
print("Aus Folgender Tabelle koennen sie die Optimalwerte entnehmen:\n")
print(zeile1, zeile2, zeile3, zeile4, zeile5, zeile6, zeile7, zeile8, zeile9, zeile10) #Gibt tabelle Aus

print("Bitte geben Sie in den folgenden Aufforderungen ihre Koerperwerte ein:")

#Groesse Wird eingegeben und gecheckt
l = input("Bitte Koerpergroesse in m eingeben:\n") 
l = float(l)

while l<1 or l> 2.5:
    print("Falsche Koerpergroesse! Bitte Anders! \n Unterstuezter Bereich von 1-2.5 m")
    l = input("Bitte Koerpergroesse in m eingeben:\n") 
    l = float(l)

#Gewicht wird eingegeben und gecheckt

m = input("Bitte Gewicht in kg eingeben: \n")
m = float(m)

while m<2 or m>250:
    print("Falsches Gewicht! Bitte Anders! \n UNterstuetzter Bereich von 2-250 kg")
    m = input("Bitte Gewicht in kg eingeben: \n")
    m = float(m)

#BMI ausrechnen

bmi= m / (l*l)

bmi_round = round(bmi, 1)

print("Ihr BMI lautet:", bmi_round)

bmi_round = float(bmi_round)

#graphische Darstellung des BMI Wertes
if bmi_round <=16:
    print(zeile1, zeile2, "---->", zeile3, zeile4, zeile5, zeile6, zeile7, zeile8, zeile9, zeile10)

elif bmi_round > 16 and bmi_round <17:
    print(zeile1, zeile2, zeile3, "---->", zeile4, zeile5, zeile6, zeile7, zeile8, zeile9, zeile10)

elif bmi_round >17 and bmi_round <18.5:
    print(zeile1, zeile2, zeile3, zeile4, "---->", zeile5, zeile6, zeile7, zeile8, zeile9, zeile10)

elif bmi_round >18.5 and bmi_round <25:
    print(zeile1, zeile2, zeile3, zeile4, zeile5, "---->", zeile6, zeile7, zeile8, zeile9, zeile10)

elif bmi_round >25 and bmi_round <30:
    print(zeile1, zeile2, zeile3, zeile4, zeile5, zeile6, "---->", zeile7, zeile8, zeile9, zeile10)

elif bmi_round >30 and bmi_round <35:
    print(zeile1, zeile2, zeile3, zeile4, zeile5, zeile6, zeile7, "---->", zeile8, zeile9, zeile10)

elif bmi_round >35 and bmi_round <40:
    print(zeile1, zeile2, zeile3, zeile4, zeile5, zeile6, zeile7, zeile8, "---->", zeile9, zeile10)

elif bmi_round >40:
    print(zeile1, zeile2, zeile3, zeile4, zeile5, zeile6, zeile7, zeile8, zeile9, "---->", zeile10)
