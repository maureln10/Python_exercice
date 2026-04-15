#Complétez le programme suivant 
# pour qu'une réduction de 5 % soit appliquée à un prix atteignant ou dépassant les 100 €.
prix = float( input("prix ? ") )

if prix >= 100 :         
    prix = prix -( prix * 5/100 )      

print("prix réduit :", prix)