####  IF #####

x =14

if x < 10:
    print("<10")
elif x < 20:
    print(">=10 and <20")
elif x < 30:
    print(">=20 and <30")
else:
    print(">=30")

####  WHILE #####
# ci può essere anche una condiziojne di for
x = 0

while x < 3:
    print(x)
    x += 1

# Se non sappiamo una condizione e dobbiamo aspettare un evento
while True:
    x = input("Inserire una stringa")

    if x == "stop":
        break  # esco da loop

    if x < "b":
        continue  # salta quello che c'è dopo e non viene eseguita la print di x

    print(x)

####  FOR #####

myList = [1, 2, 3, 4]
# stampo gli elementi della lista ( proseguo fino al suo termine )
for i in myList:
    print(i)

myString = "Python"
# stampo la stringa in verticale
for i in myString:
    print(i)

myDict = {'a': 1, 'b': 2, 'c': 3}
# Stampo solo le chiavi
for i in myDict:
    print(i)
# stampo i valori
for i in myDict.values():
    print(i)
# stampo la coppia di chiave - valore ( tupla )
for i in myDict.items():
    print(i)

#### FUNZIONE RANGE ########
# stampa start =10(incluso), fino a stop 16 (escluso), saltando 2
for i in range(10, 16, 2):  # 10 12 15
    print(i)

### LIST COMPREHENSION #####
# [ espressione for elemento in iterable if condizione ]
# scansiono elementi in un iterable, prendo solo quelli che valutano condizione, e eseguo espressione
# ritorna una lista
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newList = [n * n for n in numbers if n % 2 == 1]

### DICT COMPREHENSION #####
# Ritorna un dizionario
# {espressione su chaive : espressione su valore for elemento in iterable if condizone} => dizionario
# ord() dato un carattere, restituisce il numero corrispondente in unicode
a = 'python'
b = {k: ord(k) for k in a}  # => {'p': 112, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}
# scansiono a e metto in k, e costruisco

### SET COMPREHENSION #####
# Creo un set da una lista o una sequenza attraverso una particolare elaborazione
# { espressione fot item in iterable if condition}
# Crea un nuovo set a partire da un oggetto iterabile ( set o lista). L'insieme output set non avrà dupplicati
# elimino i doppioni da a e li metto in c
a = 'doppione'
c = {k for k in a}  # output >>> c {'d', 'o', 'n', 'e', 'i', 'p'} Le lettere presenti più di una volta vengono prese una volta sola
