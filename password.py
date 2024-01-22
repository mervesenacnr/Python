while True:
    password = input("Please enter password:")
    if not password:
        print("Please enter your password.")
    elif len(password) <= 5 or len(password) > 10:
        print("Your password must be longer than 5, shorter than 10 character.")
    else:
        print("Your password is:", password)
        break

for i in range(3): #this decides if how many times we want the for loop work
    parola = input("parola belirleyin: ")
    if not parola:
        print("parola bölümü boş geçilemez!")

    elif len(parola) in range(3, 8):
        print("Yeni parolanız", parola)
        break

    elif i == 2:
        print("parolayı 3 kez yanlış girdiniz.",
        "Lütfen 30 dakika sonra tekrar deneyin!")

    else:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

# range(ilk_sayı, son_sayı, atlama_değeri)
for i in range(0, 10, 2): # [0,10)
    print(i)
for i in range(10, 0, -1):
    print(i)
print(*range(10))
print(*range(10), sep=", ")

ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
for s in ilk_metin:
    if not s in ikinci_metin: # ilk metinde olup ikinci metinde olmayan harfleri yazdırıyoruz
        print(s)