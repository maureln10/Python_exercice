'''Complétez la fonction convertirFahrenheitEnCelsius() qui permet de convertir une température donnée en degré Fahrenheit en une température en degré Celsius.
Vous pouvez consulter la page de Wikipedia sur le Degré Fahrenheit.'''

def convertirFahrenheitEnCelsius(t):

  f = 9 /5 * t +32
  return f

print('La conversion en farenheit est : {}'.format(convertirFahrenheitEnCelsius(100)))