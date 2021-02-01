'''
Consegna 03/01/21: in un laboratorio di analisi pazienti sono sottoposti a un esame specialistico secondo l'ordine di arrivo, usa una struttura di coda 
per memorizzare i nomi dei pazienti, scrivi il programma che consenta di registrare i nomi dei pazienti, man mano che arrivano visualizza il 
nome del paziente che deve essere sottoposto all'esame perché il primo della coda in attesa.
'''
pazienti = []

def menu():
    print("______________________________________________")
    print("1. Inserisci nuovo paziente")
    print("2. Analisi primo paziente della fila")
    print("3. Visualizza coda pazienti")
    print("4. Fine")
    print("______________________________________________")

def operazioni():
    operazione = int(input("Scegli l'operazione che desideri fare: "))
    return operazione

def aggiungi():
    nome = input("Inserire il nome del paziente: ")
    pazienti.append(nome)

def pop():
    if len(pazienti) == 0:
        print("Non ci sono pazienti in coda")
    else:
        nome = pazienti.pop(0)
        print("Avvio analisi del paziente:", nome)

def visualizza():
    if len(pazienti) == 0:
        print("Non ci sono pazienti in coda")
    else:
        conto = 0
        for paziente in range(len(pazienti)):
            conto += 1
            nome = pazienti[paziente]
            print("paziente", conto, ":", nome)

def main():
    while True:
        menu()
        operazione = operazioni()
        if operazione == 1:
            aggiungi()
        elif operazione == 2:
            pop()
        elif operazione == 3:
            visualizza()
        elif operazione == 4:
            print("Fine analisi")
            break
        else:
            print("operazione inserita non valida")

main()