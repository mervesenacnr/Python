ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ZeroDivisionError:
    print("Bir sayıyı 0'a bölemezsiniz!")
except ValueError:
    print("Lütfen sadece sayı girin!")

try:
    bölünen = int(input("bölünecek sayı: "))
    bölen = int(input("bölen sayı: "))
    print(bölünen/bölen)
except ZeroDivisionError:
    print("bir sayıyı 0'a bölemezsiniz")
    raise

giriş = input("Merhaba! Adın ne? ")
if len(giriş) == 0:
    raise AssertionError("İsim bölümü boş.")
print("Hoşgeldiniz.")

giriş = input("Merhaba! Adın ne? ")
assert len(giriş) != 0 , "İsim bölümü boş."
print("Hoşgeldiniz.")