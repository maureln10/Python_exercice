#Complétez l'instruction conditionnelle pour que le programme affiche la réponse qui convient.
#Vous utiliserez l'opérateur modulo % qui donne le reste de la division euclidienne.
#Ainsi 26 % 10 == 6 puisque 26 divisé par 10 fait 2 et il reste de 6.

n = int( input("Saisir un nombre entier :") )

if n % 2 == 0:
   print(n, "est un nombre pair")
else:
   print(n, "est un nombre impair")