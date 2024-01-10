tr_harfler = "şçöğüİı"

for harf in tr_harfler:
    print(harf)

tr_harfler = "şçöğüİı"
a = 0
print("---------------------------")
while a < len(tr_harfler):
    print(tr_harfler[a], sep="\n")
    a += 1
print("---------------------------")
sayılar = "123456789"
for sayı in sayılar:
    print(int(sayı) * 2)
print("---------------------------")
sayılar = "123456789"
for i in sayılar:
    if int(i) > 3:
        print(i)
print("---------------------------")
tr_harfler = "şçöğüİı"
parola = input("Parolanız: ")
for karakter in parola:
    if karakter in tr_harfler:
        print("parolada Türkçe karakter kullanılamaz")
print("---------------------------")
while True:
    parola = input("Bir parola belirleyin: ")

    if not parola:
        print("parola bölümü boş geçilemez!")

    elif len(parola) > 8 or len(parola) < 3:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

    else:
        print("Yeni parolanız", parola)
        break
print("---------------------------")
print("""
Basit bir hesap makinesi uygulaması.

İşleçler:

    +   toplama
    -   çıkarma
    *   çarpma
    /   bölme

Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")

veri = input("İşleminiz: ")
hesap = eval(veri)

print(hesap)