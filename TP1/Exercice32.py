'''
Un parc d'attractions affiche les tarifs suivants :

8,50 € par enfant
12,00 € par adulte
Vous devez écrire une fonction prix() qui renvoie le prix total à payer, à partir du nombre n d'enfants et du nombre p d'adultes.
'''
n =  int(input('Entrer le nombre d\' enfant :'))
p =  int(input('Entrer le nombre d\'adulte :'))

def prix(n, p):
    total = n * 8.5 + p * 12
    return total
resultat = prix(n,p)

print(f'le total a payer est :{resultat} £') 