
#Toda lista se debe escribir en plural


arboles=['ceiba','yarumo','manzano','guayacan']

municipios=['Medellin','titiribi','Carolina del principe']

hectareaSembradas=[2500,500,1200]

lluviasMayoresA500=[False,True,True]

#Recorriendo un arreglo..
#Acceder de forma dinamica al contenido de un arreglo
#Para recorrerlo debo utilizar un ciclo o buble o loop

#Ciclo while(mientras) 
'''contador=0
while contador<10:
contador=contador+1
print("estoy triunfando...")'''


#Ciclo For(Para)
for variableiteradora in range(10):
    print(variableiteradora)

    #Recorrer dinamicamente un arreglo usando un For each(Para cada uno)
    for arbol in arboles:
        print(arbol)

    for municipio in municipios:
        print(municipio)   