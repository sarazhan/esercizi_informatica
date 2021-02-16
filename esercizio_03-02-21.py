'''
Consegna: si definisca una funzione che preso un dizionario di studenti e voti, restituisca un dizionario 
con gli studenti suddivisi per intervalli di media di voto: k1 (18,23), k2(24.26) e k3(27,30).
Nel calcolo della media la lode permette di arrotondare all'intero successivo, nel caso in cui
nella lista dei voti non sia presente una lode l'arrotondamento è per difetto
'''

from statistics import mean
import math

def nuovo_diz(media):
    n_diz = {}
    if media in range(18,24):
        n_diz["18-23"] = media
    elif media in range(24, 27):
        n_diz["24-26"] = media
    elif media in range(27, 31):
        n_diz["27-30"] = media
        
    return n_diz

def main():
    lunghezza = int(input("Quanti studenti vuoi inserire: "))
    for n in range(lunghezza):
        studente = input("Inserire nome studente: ")
        voti = input("Inserisci voti dello studente separati da uno spazio: ")
        voti = [int(i) for i in voti.split()]
        media = mean(voti)
        lode = input("Scrivi si/no per la Lode: ")
        if lode == "no":
        	media = math.trunc(media)
        else:
        	media = math.trunc(media+1)
        n_diz = nuovo_diz(media)
        print("Studente:", studente, n_diz)

main()
