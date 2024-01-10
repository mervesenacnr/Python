# This  is my first Python project named
# "Practical exercise 1: Plan an exciting adventure with a new friend"
name_a = "Amir: "
message_a = "Hi my name is Amir. Nice to meet you!"
print(name_a, message_a)

name_b = "Merve: "
message_b = "Hi I'm Merve. Nice to meet you too. Let's get to know each other."
print(name_b, message_b)

age_a = 20
height_a = 1.76
hair_color_a = "brunette"
hometown_a = "Iran"
where_lives_a = "Turkey"

print(name_a, "I am", str(age_a), "years old,", str(height_a), "tall", hair_color_a, "guy from",
      hometown_a, "but I currently live in", where_lives_a)

print("What about you? Tell me about yourself.")

age_b = 22
height_b = 1.62
hair_color_b = "red"
hometown_b = "Izmir"
where_lives_b = "Istanbul"

print(name_b, "I am", str(age_b), "years old,", str(height_b), "tall", hair_color_b, "hair girl from",
      hometown_b, "but I study in", where_lives_b)

print(name_a, "So... What are the places you want to go for dinner? And what do you want to eat?")

favorite_places = "Beşiktaş Kadıköy Taksim Eminönü Üsküdar"
favorite_dinner = "döner lahmacun ıslakhamburger balıkekmek sansebastian"
print(name_b, "I love", favorite_places.split(), "in Istanbul. And we need to try",
      favorite_dinner.split(), "!")

place_list = favorite_places.split()
dinner_list = favorite_dinner.split()

print(name_a, "Select one!")
print(name_b, "It's hard to select actually, we can go", place_list[0:3], "and eat",
      dinner_list[2:5], "What do you think? You choose.")
"""
Listeleme Kuralı:
Diyelim ki listemizde 5 item var. Bu 5 itemden bir kaçını seçmek istiyoruz, itemlerin sıra numaraları şöyledir:

null    item1, item2, item3, item4, item5  null
 0        1      2      3      4      5     6
 
 ilk 3 itemi ekrana yazdırmak istersek: 
 
 list[0:3] kodunu kullanırız ve ekrana item1,item2,item3 gelir.
 
 Bu da istediğimiz item kümesinin formülünün ( x, y ] olduğunu gösterir.
"""

import random
print(name_a, "Then we'll go to", random.choice(place_list), "and eat", random.choice(dinner_list))

print(name_b, "Good choise Amir! Let's do that!")

import datetime
an = datetime.datetime.now()
print(name_a, "When are you available?")

print(name_b, "Right now the time is:", an.time(), "I'm available after ")
print(input())

print(name_a, "Good! See you there!")
print(name_b, "See you!")
