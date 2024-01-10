# functions

def sum(number1, number2):
    answer = number1 + number2
    return answer

result = sum(3, 5)
print(result)

# keyword of capitalize()

def greetings(correction, name, surname):
 if correction == True:
  capitalized_name = name.capitalize()
  capitalized_surname = surname.capitalize()
  print('Hello,', capitalized_name, capitalized_surname)
 else:
  print('Hello', name, surname)

greetings(True, 'meRvE', 'ÇınAR')
greetings(False, 'meRvE', 'ÇınAR')

def favourite_car(brand, model, color):
    print('My favourite car is', brand, model, 'in the color', color)

favourite_car('McLaren', 'Senna', 'blue')
favourite_car(model='Senna', color='blue', brand='McLaren')

# Global keywordü ile fonksiyonun içerisinde değiştirilmiş değişkeni fonksiyonun dışına tanımlayabiliriz