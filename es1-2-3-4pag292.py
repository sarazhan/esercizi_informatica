class atleta():
    def __init__(self, nome, cognome, visita, squadra):
        self.nome = nome
        self.cognome = cognome
        self.visita = visita
        self.squadra = squadra
    def effettua_visita(self) :
    	self.visita = True
    def info(self):
    	print("L'atleta si chiama", self.nome, self.cognome,"\n Visita medica:", self.visita, "\n Gioca nella squadra:", self.squadra)
    	
atleta = atleta("Maria", "Gianfranca", False, "Fragola" )
atleta.info()
atleta.effettua_visita()
atleta.info()
