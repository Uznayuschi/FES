###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

l = float(input('Inserteix nivell: '))
c = ''
if l >= -50 :
    c = 'excel·lent'
if -50 > l >= -67 :
    c = 'bona'
if -67 > l >= -75 :
    c = 'feble'
if -75 > l :
    c = 'molt feble'

print(f"Connexió %s." % (c))

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

p = float(input('Inserteix nivell: '))
c = ''
if p > -8 :
    c = 'massa alt'
elif p < -27 :
    c = 'massa baix'
else :
    c = 'acceptable'

print('Nivell ' + c + '.')
    
# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

a = int(input('GB de trafic en mes: '))
if a <= 20 :
    print('El consum esta en el marge de 20GB.')
else:
    print(f'El consum supera el marge per %i GB.' % (a - 20))

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

ind_fibra = input("Està encès l'indicador del terminal òptic? s/n: ")
ind_connexio = input("Està encès l'indicador de connexió a Internet? s/n: ")
c = ''
if ind_fibra == 'n' :
    c = "Comprova el cable òptic."
elif ind_connexio == 'n' :
    c = "Comprova el servei del proveidor."
elif ind_fibra == 's' & ind_connexio == 's' :
    c = "La connexió sembla funcionar correctament."
print(c)
                  
# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

b = int(input("El percentange de bateria restant: "))
c = ''
if 0 <= b <= 100 : 
    if b < 20 :
        c = 'crítica'
    elif 20 <= b <= 49 :
        c = 'baixa'
    else:
        c = 'suficient'
    print("Carrega de bateria és %s." % (c))
else:
    print("Valor fora del rang.")
