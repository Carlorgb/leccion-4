
import requests , json

url = "https://pokeapi.co/api/v2/pokemon"

response =  requests.request ("GET" , url)

#print( response.text)





mi_diccionario = json . loads (response . text)



resultados =  mi_diccionario ["results"]

print (mi_diccionario  ["results"] [0] )

for resultado in resultados :
    print (resultado)


