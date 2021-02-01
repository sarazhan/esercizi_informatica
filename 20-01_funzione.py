def fuoco_para(a, b, c):
    fx = (1-b**2)+(4*a*c)
    fy = -b/(2*a)
    return fx, fy

def vertice_para(a,b,c):
    vx = -b/(2*a)
    vy = (4*a*c-b**2)/(4*a)
    return vx, vy

a = int(input("Quanto vale a? "))
b = int(input("Quanto vale b? "))
c = int(input("Quanto vale c? "))

Fuoco = fuoco_para(a, b, c)
Vertice = vertice_para(a,b,c)
print("Fuoco",Fuoco," Vertice", Vertice)