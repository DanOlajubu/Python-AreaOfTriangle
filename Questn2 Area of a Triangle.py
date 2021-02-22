#Project 2 - Calculate the area	of a triangle - from the instructor below
#Will need input from the user, need the height	and base values
#Might want to use "float" to be more precise in the calculations
#Area =	(1/2*B *h)

print("Solution from the internet javaTpoint below")
#Mathematical formula:

# Three sides of the triangle is a, b and c
#uncomment below to take input from the user

a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# calculate the semi-perimeter

s = (a + b + c) / 2  
  
# calculate the area by finding the square root

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("The area of the triangle is %0.2f" %area)   
