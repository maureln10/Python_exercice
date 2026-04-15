#Modifiez le programme pour qu'il affiche la réponse qui convient 
# suivant la longueur et la largeur du rectangle.
longueur = float( input("Longueur ? : ") )
largeur = float( input("Largeur ?  :") )

if longueur == largeur :
  print("Le rectangle est un carré.")
else :
 print("Le rectangle n'est pas un carré.")