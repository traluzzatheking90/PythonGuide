##### LISTE ######
# Le liste possono contenere anche oggetti di tipo differente.

myList = [] # Lita vuota oppure sotto
myList = list()

myList = [12, 23, 43]  # Lista piena

myList[2] = 0  # >>> myList [12, 23, 0]

# Offset

myList[1]  # >>> 23
myList[-1]  # >>> 43

# Liste di liste
# bidimensionale

myList = [[1, 2], [3, 4], [4, 5]]
myList[1][1]  # >>> 4

# Estrazione da una lista slice
myList = [12, 23, 43]

myList[:2]  # >>> [12, 23]

# Lughezza Lista
len(myList)  # 3

# Inserimento di una lista

myList = [10, 20, 30]
myList.insert(2, 50)  # [10, 20, 50, 30]
myList.append(60)  # [10, 20, 50, 30, 60]
del myList[1]  # [10, 50, 30, 60]
20 in myList  # [10, 50, 30, 60]  False

# Due nomi una lista
myList = [10, 20, 30]
myList2 = myList
myList2[1] = 50  # >>> myList  [10, 50, 30] >>> myList2 [10, 50, 30]

# Funzione copy
myList = [10, 20, 30]
myList2 = myList.copy()
myList2[1] = 50  # >>> myList  [10, 20, 30] >>> myList2 [10, 50, 30]

### TUPLE ###
# Sequenza, come lista, ma immutabile (non posso modificarli)

medal = ()  # creazione di una tupla vuota
medal = tuple()  # creazione di una tupla vuota
medal = ('oro', 'argento', 'bronzo')  # oppure
medal = 'oro', 'argento', 'bronzo'

# tuple unpacking
# Il tuple unpacking richiede che per ogni elemento della tupla sia indicata una
# corrispondente variabile (invece questa tupla ha tre elementi, ma solo due variabili
# a disposizione per l'unpacking).

o, a, b = medal  # o = oro, a = argento, b = bronzo

### DICTIONARY ###
# Non c'è ordine. Key - Value

myDict = {}     # Costruzione vuota
myDict = dict()

myDict = {
    "primo": 10,
    "secondo": 20,
    "terzo": 30
}
# Aggiungere un elemento o modificare se la chiave non esiste
myDict["quarto"] = 40

# cancellare un elemento
del myDict["secondo"]
# tutti gli elementi
myDict.clear()
myDict = {}

# Se un oggetto è dentro ad un dizionario ( la chiave )
"terzo" in myDict

# Dizionario con l'uguale alla fine puntano allo stesso oggetto
# Per dupplicare usare copy

myDict2 = myDict.copy()

# dict items = funzione che ritorna degli elementi tipo tupla/iteratore di un dictionary
d1 = {10: 'a', 20: 'b'}
d2 = {30: 'c'}

l1 = d1.items()   # l1 >>>> dict_items([(10, 'a'), (20, 'b')])
l2 = d2.items()
# Da un oggetto di tipo dict items posso ricostruire un dizionario
d3 = dict(l1)  # >>> d3{10: 'a', 20: 'b'}
d3.update(dict(l2))
# >>> d3  {10: 'a', 20: 'b', 30: 'c'}

### SET ### insime cotiene una serie di elementi che devono essere univoci ( chiavi ) per operazioni su insieme

mySet = set() # set vuoto unico modo
mySet = set([10, 20, 30, 40])

mySet.add(30)

## Frosenz set ( set immutabile )

mySet = frozenset([10, 20, 30, 40])
#  non ho l'attributo add per la classe frosenset

30 in mySet

## Sugli insiemi si fanno operazioni di intersezione e unione
mySet = set([10, 20, 30, 40])
mySet2 = set([40, 30, 70, 80])

mySet & mySet2 ## intersezione {40, 30}
mySet | mySet2 # unione tra due insiemi {70, 10, 80, 20, 30, 40}
mySet - mySet2  # sottrazione {10, 20} Tutti quelli che appartengono al prima ma non al secondo
mySet ^ mySet2  #Or esclusivo  contrario dell'unione
