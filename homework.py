# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

x = 0
while x**3 < 1000:
    print(x**3)
    x = x + 1
    
# Get first prime numbers up to 100

x = 5
prime = x 
if prime > 1:
    for i in range(2, prime//2):
        if (num % i) == 0:

        else:
            print(prime)
#NEED HELP
    


# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
    
age = input('How old are you? ')

if int(age) < 18:
    print('kids')
elif int(age) > 65:
    print('seniors')
else:
    print('adults')
    