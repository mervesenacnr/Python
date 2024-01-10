# if , else statements

celsius = 18

if celsius > 30:
    print('Hot 🔥')

if celsius > 20:
    print('Good 🤙')

else:
    print('Cold ⛄')

drivers_licence = True
age = int(input('Your age: '))

if age >= 18:
    if drivers_licence:
        print('You can drive a car.')
    else:
        print('You need to go drivers licence course to drive a car.')

else:
    print('You have to get older (at least 18) to drive a car.')


# for loops

random = 'mklfdöçmsdf'
for i in random:
    print(i)
print('End of the random.')

for i in range(1,101):
    if i % 5 == 0:
        print(i)
print('Loop has been completed.')

# while loop
number = 1
while number < 3:
    if number > 1:
        print('There')
    else:
        print('Hello')
    number += 1
print('End of the loop ')