diz = {}
diz["asino"] = 11111
diz["pavone"] = 33333
diz["topo"] = 88888
diz["zebra"] = 66666

def nome(diz):
        while True:
            nome = input("Scrivi un nome in minuscolo: ")
            if nome not in diz:
                print("Non esiste questa persona nella tua rubrica")
            else:
                numero = diz[nome]
                print(numero)
            controllo = input("Scrivi . per interrompere il programma, altrmenti premi spazio: ")
            if controllo == ".":
                break
nome(diz)