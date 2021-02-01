import math
def trapezio(a, b, c):
    area = ((b+a)*c)/2
    lati_obliqui = math.sqrt(c**2+(b-a)**2)
    perimetro = a+b+lati_obliqui
    return area, perimetro

def main():
    while True: 
        base_min = int(input("Per calcolare l'area e il perimetro di un trapezio, inserisci la base minore: "))
        if base_min<0:
            print("Si prega di inserire numeri positivi")
        else:
            base_mag = int(input("Inserisci la base maggiore: "))
            if base_mag <0:
                print("Si prega di inserire numeri positivi")
            else:
                altezza = int(input("Inserisci la misura dell'altezza: "))
                if altezza <0:
                    print("Si prega di inserire numeri positivi")
                else:
                    print(trapezio(base_min, base_mag, altezza))
                    break
main()