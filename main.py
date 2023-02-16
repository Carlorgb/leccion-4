print("Hello")

palabra = "CARLOS"

print (palabra[0])  #para crear un indece se debe recordar que los "(va dentro de los parentesis[parentesis cuadrados])" llaman a cada digito que se requiere se inicia de cero   
print (palabra [1])
print (palabra [2]) 
print (palabra [3])
print (palabra [4])
print (palabra [5])


for letra in palabra: # para cada letra en palabra haga tal cosa significa for_____ in____
    print (letra + "G" , "B")

marcas = ["BMW" , "Honda" , "Nissan"]

for marcas in marcas:
    print(marcas)
palabra = "Examen"
indice =0 
for letra in palabra:
    print (indice , letra )
    indice = indice + 1

for indice , letra in enumerate (palabra) : #enumerate funcion de pyton sirve enumerar el indice 
    print (indice , palabra)