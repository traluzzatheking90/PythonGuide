#### FUNZIONI ######
# Insieme di istruzioni che puù essere eseguita su richiesta e che è identificata da un nome.
# Un istruzione in Python è anche un Oggetto, chiamato Callable object


def function_name(parameters):
    # Suite di una funzione è composta dal blocco di istruzioni di una funzione
    print("Statements")
    # Statements


# PARAMETRI POSIZIONALI O OBBLIGATORI
# Paramtri che devono essere obligatoriamente forniti alla chiamata di una funzione


def my_func(a, b, c, d):
    print(a, b, c, d)


# Chiamata di una funzione con paramtri keyword
# Posso chiamare specificatamente i parametri con l'identificatore della variabile, quindi anche i ordine sparso
# Posso fare una chimamata mista a patto che all'inizio sia tutto inordine e in fondo i parametri keyword
my_func(10, 20, c=10, d=4)

# PARAMETRI OPZIONALI
# C e D sono opzionali, se non li dichiaro prendo ivalori di default A e B sono obligatori


def my_func(a, b, c=3, d=4):
    print(a, b, c, d)

# PARAMETRI ARGS
# I parametri vengono assegnati tutti sotto forma di tupla.


def my_func(*args):
    print(args)


my_func(1, 45, 56, "Ciao")  # -> é una tupla args quindi posso mettere ciò che voglio  (1, 45, 56, 'Ciao')


def my_func(a, b, *args):  # Possibile avere anche parametri posizionali più un parametro args
    print(a, b,args)       # Args deve essere l'ultimo


my_func(1, 45, 56, "Ciao")  # 1 45 (56, 'Ciao') a b e la tupla

# Keyword args **kwargs keyword Argumetns
# Numero variabile di elementi contenuti in un dizionario


def my_func(**kwargs):
    print(kwargs)


my_func(a=1, b=2, c=3) # -> Mi ritoro {'a': 1, 'c': 3, 'b': 2} con chiave i nomi e valori