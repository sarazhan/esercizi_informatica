'''
esercizio pagina 73 numero 24: alla fine dellla giornata di elezioni per il balotaggio tra due candidati, si acquisiscono i voti ottenuti
dai due candidati. Scrivi il programma che calcoli le percentuali ottenute da ciascun candidato e comunichi il nome del vincitore
'''
votoa = int(input("Voti del primo candidato: "))
votob = int(input("Voti del secondo candidato: "))
somma = votoa + votob
percentualea  = (votoa/somma)*100
percentualeb = (votob/somma)*100

print(" Le percentuali sono :  Il primo", percentualea, "%    Il secondo", percentualeb, "%")
if votoa> votob: 
    print("Il vincitorere è il primo candidato")
elif votoa == votob:
    print("C'è stato un pareggio")
else : 
    print("Ha vinto il secondo candidato")
