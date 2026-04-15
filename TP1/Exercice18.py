#'''Eloïse a un choisi un nombre secret n puis elle a appliqué l'algorithme suivant :

#J'ai soustrait 5 à mon nombre
#J'ai ensuite multiplié le total par 4
#Et pour finir, j'ai soustrait mon nombre au résultat
#Elle a noté x le résultat obtenu.
#Votre défi consiste à écrire la formule permettant de retrouver le nombre secret n à partir de x.

x = 1

n = 5 - x
n *= 4
n-=x
print(n)
