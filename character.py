site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"
for isim in site1, site2, site3, site4:
    print("site: ", isim[4:-4])

isim = input("isminiz: ")
for i in range(len(isim)):
    print("isminizin {}. harfi: {}".format(i+1, isim[i]))

kardiz = "Sana Gül Bahçesi Vadetmedim"
print(kardiz[::-1]) #print each item in reverse
print(kardiz[7:4:-1])
kardiz = "istanbul"
print(kardiz[0:8:1])
print(kardiz[0:8:2])
print(kardiz[::2])
print(kardiz[::-1])
print(kardiz[::-2])

for i in sorted("kitap"):
    print(i, end="")

print(sorted("elma"))

"""
import locale
locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254") #Windows için klavye yüklemesi
"""
site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"
for i in site1, site2, site3, site4:
    print("http://", i[4:], sep="")

kardiz = "istihza"
print("İ" + kardiz[1:])
print(id(kardiz))
