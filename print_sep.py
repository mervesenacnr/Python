#Sep: print() fonksiyonunun içerisine yazılan stringlerin arasındaki boşlukları belirleyen bir özelliktir.

print("http://", "www.", "google.", "com")
print("http://", "www.", "google.", "com", sep=" ")
print("http://", "www.", "google.", "com", sep="")

print("Adana", "Mersin", sep="-") #sep, stringlerin arasındaki boşlukları doldurmak için de kullanılır

print("bir", "iki", "üç", "dört", "on dört", sep=" " + "mumdur" + " ")
print("bir", "iki", "üç", "dört", "on dört", sep=" mumdur ")

"""
sep ifadesi, İngilizcede separator (ayırıcı, ayraç) kelimesinin kısaltmasıdır. 
Dolayısıyla print() fonksiyonundaki bu sep parametresi, ekrana basılacak öğeler arasına
hangi karakterin yerleştirileceğini gösterir. Bu parametrenin öntanımlı değeri bir adet boşluk karakteridir (” “).
Yani siz bu özel parametrenin değerini başka bir şeyle değiştirmezseniz, 
Python bu parametrenin değerini bir adet boşluk karakteri olarak alacak ve ekrana basılacak öğeleri
birbirinden birer boşlukla ayıracaktır. Ancak eğer biz istersek bu sep parametresinin değerini değiştirebiliriz.
Böylece Python, karakter dizilerini birleştirirken araya boşluk değil, bizim istediğimiz başka bir karakteri 
yerleştirebilir. 
"""