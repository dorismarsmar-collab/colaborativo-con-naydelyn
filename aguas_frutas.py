'''
#programa que permite beber bebidas
# solicitan unja opcion para elegir bebidas
#pregunta cantidad de bebida 
#muestra total a pagar
'''

print("=============================")
print("Aguas frescas UAGro")
print("Menu de bebidas")
print("1. Agua de mango - $40")
print("2.Agua de jamaica - $45")
print("3. Agua de horchata -$35")
print("===============================")

opcion= int(input("elige una opcion del menu: "))
cantidad= int(input("Cuantos litros?"))

if opcion ==1:
    bebida="Agua de mango"
    precio= 40
elif opcion==2:
    bebida="Agua de jamaica"
    precio= 45
elif opcion==3:
    bebida="Agua de horchata"
    precio= 35
else:
    bebida="no existe la bebida"
    precio=0
if precio>0:
    total=precio * cantidad
    print("f{cantidad} de")
    print(f"total a pagar: {total}")
else:
    print("no existe la bebida")