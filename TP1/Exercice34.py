'''Modifiez le programme suivant pour qu'il affiche la table de multiplication de 5, pour les nombres de 0 à 10 inclus.

5 * 0 = 0
5 * 1 = 5
...
5 * 10 = 50'''

def table_multi(n):
    for i in range(11):
        print(f'{n} * {i} = {n*i}')

table_multi(5)