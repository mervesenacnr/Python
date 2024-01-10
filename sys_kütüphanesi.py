import sys

dosya = open("deneme.txt", "w")
print("Ben Python", file=dosya)
dosya.close()

"""
print("Tahir olmak da ayıp değil", "Zühre olmak da",
sep=" ", end="\n", file=sys.stdout)

normalde print() kalıbını kullanırken ne sep ne de end kullanırız, yaptığımız kodlamanın
hızlı ve kısa olmasını istediğimiz için, ancak her print işleminde python programı içerisinde şu 3 komutu içerir:
-sep
-end
-file

"""

f = open("kisisel_bilgiler.txt", "w")
"""
print("Merve Sena Cinar", file=f)
print("22", file=f)
print("Izmir", file=f)
f.close()

Bu kod satırında kullandığımız close() komutunun yerine geçen bir komut daha vardır:
flush = True/ False
True halindeyken dosyaya kaydetmek istediğimiz bilgileri işler
False halindeyken bilgiler alınır ama programın tamponunda bekletilir 
"""

print("Merhaba Dunya!", file=f, flush=True)

print(*"Linux", sep=".") #print edeceğimiz yazının önüne yıldız koymak harfleri ayırırken kolaylık sağlar

print("L", "i", "n", "u", "x", sep=".")

print(len("Galatasaray"))