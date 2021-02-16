def fatturato():
    nord = int(input("Fatturato Nord: "))
    centro = int(input("Fatturato Centro: "))
    sud = int(input("Fatturato Sud: "))
    isole = int(input("Fatturato Isole: "))
    totale = nord + centro + sud + isole
    print("Totale fatturato:", totale)
    percentuale_nord = (nord*100)/totale
    percentuale_centro = (centro*100)/totale
    percentuale_sud = (sud*100)/totale
    percentuale_isole = (isole*100)/totale
    print("Percentuale Nord sul totale:", percentuale_nord)
    print("Percentuale Centro sul totale:", percentuale_centro)
    print("Percentuale Sud sul totale:", percentuale_sud)
    print("Percentuale Isole sul totale:", percentuale_isole)
fatturato()