# esercizio numero 32 pag. 73: Calcolare l'equazione ax+b=0 con a e b, variabili, secondo la tabella.
a = int(input("Per calcolare l'equazione ax+b=0, serve sapere a che vale: "))
b = int(input("e b: "))
if a == 0 and b == 0:
    print("Equazione indeternminata")
elif a == 0:
    print("Equazione impossibile")
elif b == 0:
    print("x = 0")
else:
    calcolo = b/a
    print("x = -%s" %calcolo)