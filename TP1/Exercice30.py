'''
Créez la fonction circonference de paramètre rayon qui calcule et renvoie le périmètre du cercle de rayon donné.
On définira la constante PI de valeur 3.1415926 dans la fonction elle-même. '''

Pi =  3.1415926
r = 5

circunference = round( Pi *r**2)
print('la circonference est : {}'.format(circunference))