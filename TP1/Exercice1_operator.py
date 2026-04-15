####  Area of triangle ###

Base = 20
Height = 10

Area = round(0.5 * Base * Height)

# result

print('The area of this triangle is :', Area)

# perimeter

a = 5
b = 4
c = 3
Perimeter = a + b +c 

# result
 
print('The perimeter of this triangle is :', Perimeter)




#### Area  and perimeter of rectangle ###

Length = float(input('Please enter a lenght:'))
Widith = float(input('Please enter a widith:'))

Area = round(Length * Widith )
Perimeter = round(2*(Length + Widith))

# result

print('THe area of this rectangle is :', Area)
print('THe perimeter of this rectangle is :', Perimeter)




###  area of circle  ###
pi = 3.14
r = float(input('Plaese enter a radius :'))

Area =  pi * r**2
Circumference  = round(2 * pi * r)

# Result 

print('The area of this circle is :',Area)
print('The perimeter of this circle is :',Circumference)



### slope  ###

# Equation : y =  2*x - 2

m = 2 
b = - 2

print("The slope is :", m)

# y- intercept 
x = 0
y = m * x + b

print('y-intercept is', y)

# x- inercept

y = 0

x = -b / m

print('x-intercept is',x)



### slop and Euclidean distance ###

# The slope : m = y2-y1 / x2 -x1

x1 , y1 = 2 , 2
x2 , y2 = 6, 10

m = (y2-y1) / (x2-x1)

print('The slope is :', m)

# Euclidean distance
import math
dx = x2 - x1 
dy = y2- y1

d =math.sqrt(dx** 2 / dy**2) 

print('The euclidean disatnce is :', d)


### Discriminant ###

import math  

# Equation : y = x**2 + 6x + 9
a = 1
b = 6
c = 9

# Discriminant
d = b**2 - 4*a*c
print('The discrimniant is :',d)
# Solutions
x1 = (-b + math.sqrt(d)) / (2*a)
x2 = (-b - math.sqrt(d)) / (2*a)

print(" The result is :", x1, x2)


#### Length of words and comparison ###

word1 =  'Python'
word2 = 'Dragon'

# Length

Length1 = len(word1)
Length2 = len(word2)

# 'on' not in words 

result1 =('on' not in  word1 ) and ('on' not  in word2 ) 


print(Length1 != Length2)

result =('on' in  word1 ) and ('on' in  word2 ) 

print(result)
print(result1)


### check if ###

sentence = 'I hope this course is not full of jargon. '

check = 'jargon' in sentence

print(check)



#### Find length ###

text = 'Python ' 
text_len = len(text)

# converting
convert_float = float(text_len)
convert_str = str(text_len)

print(text_len)
print(convert_float)
print(convert_str)

### Even sentence ###

text = 'Python'

text_len = len(text)

num =  text_len

print(num % 2 == 0)


### check division 7 by 3  equal to int converted of 2.7 ###

c = 2.7
a = 7 
b = 3

r = a / b 

# Verification

verif = r == c

print(verif)


### check if type of 10 equal to '10' ###

a = 10 
 
b = '10'

print(a==b)


## check if int (9.8) equal to 10 ##

a = int(9.8)
 
b = 10

print(a==b)



### Calculate pay for person ###

hours = 40

rate_per_hour = 28

pay = hours * rate_per_hour 

print('Your weekly earning is', pay)


### Calculate number of second live by a person ###

year = int(input('Enter your age :'))

seconds = year * 365 * 24 * 60 * 60

print(f'You have lived for {seconds} seconds.')

### table ###

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)