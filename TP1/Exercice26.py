#Une boutique de photocopies propose le tarif suivant :

#plein tarif : 0,08 € / photocopie, les 50 premières
#tarif réduit : 0,06 € / photocopie, les suivantes
#Écrire une fonction calculerPrix() qui prend en paramètre le nombre n de photocopies
#  à réaliser et renvoie le prix à payer en euro pour toutes ces photocopies.
n =  int(input('The number of copies :'))
def calculerPrix(n):
   if n <= 50 :
        prix =  n*0.08
    
   else:
        prix = n* 0.08 + (n -50)* 0.06
   return  prix 
print(calculerPrix(n),'£')