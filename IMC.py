p= input ("Peso")
a= input("Altura")

fp = float (p)
fa = float (a)
    
x = fp/(fa*2)

if x < 18.5:
    print (x,"Abaixo de peso")
elif 18.5 < x <= 24.9:
    print (x,"Normal")
elif 25 <= x <= 29.9:
    print (x,"Sobrepeso")
elif 30> x < 99:
    print (x,"Obeso")
elif x> 100:
