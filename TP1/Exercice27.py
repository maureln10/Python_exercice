#Complétez le programme suivant en écrivant la fonction maximum() dont les paramètres sont trois nombres a, b, 
# c et qui renvoie le plus grand des ces trois nombres.
def maximum(a, b, c):
    if a > b :
       return a
    elif  b > c:
       return b
    else :
       return c

x = float( input("1er nombre ?") )
y = float( input("2nd nombre ?") )
z = float( input("3e  nombre ?") )

print("Le plus grand est", maximum(x,y,z))