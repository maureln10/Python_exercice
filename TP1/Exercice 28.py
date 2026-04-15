#Complétez la fonction tarif(age) pour qu'elle renvoie la chaîne de caractères :

#"plein"   lorsque age est supérieur ou égal à 18
#"reduit"   lorsque age est compris entre 12 inclus et 18 exclu
#"gratuit"   lorsque age est inférieur à 12

def tarif(age):
  if age >= 18 :
      return "plein"

  elif 12 <= age < 18 :
        return " reduit "
  else:
      return " gratuit"


age = int(input("Quel est votre âge ?"))

print("Vous bénéficiez du tarif :", tarif(age))
