#Corrigez le programme suivant pour qu'il affiche :

#"La porte s'ouvre..." lorsqu'on répond "Sésame"
#"La porte reste fermée !" dans le cas contraire

mdp = input("Mot de passe, SVP ? : ")

if mdp == 'Sésame ':
   print("La porte s'ouvre...")
else :
  print("La porte reste fermée !")