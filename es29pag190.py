#Consegna 18/02/21: scrivi un programma che legga un reddito da tastiera e calcoli dellimporto dell'imposta 
#sul reddito e la tassazione media. 
reddito = int(input("Quant'è il tuo reddito? "))

if reddito<15000:
    tassa = (reddito*23)/100
elif reddito in range(15000,27999):
    tassa = 3450+(reddito*27)/100
elif reddito in range (28001,54999):
    tassa = 6960+(reddito*38)/100
elif reddito in range (55001, 74999):
    tassa = 17220+(reddito*41)/100
elif reddito>75000:
    tassa = 25420+(reddito*43)/100
    
media = tassa*100/reddito
round(media,1)
print("La tassazione totale è di:", tassa,"e la tassazione media è di:", media)
