#Realiza un programa que dependiendo de una lista de nombres te pregunte si ese wey es joto y sí es joto que mande a llamar una función que le miente la madre 50 veces, sí no es joto que mande a llamar una función que le imprima que se salvó
lista_de_jotos = ["sofia","camila","alondra","valeria","ximena","paola","yolanda","santiago","eder","benjamin","leonardo","alejandro","regina","diego","daniel","javier"]
i = 0
def preguntar_su_nombre_y_decir_si_es_joto (joto):
    print("eres extremadamente homosexual " + joto)
    
joto = input("cual es su nombre? : ")

if joto in lista_de_jotos:
    while i < 50:
        preguntar_su_nombre_y_decir_si_es_joto (joto)
        i = i + 1

else:
    print("te salvaste papu")