#file: print() fonksiyonuna verilen karakter dizisi ve/veya sayıların, yani parametrelerin nereye yazılacağını belirtir

dosya = open("deneme.txt", "w")
print("Ben Python, Monty Python!", file=dosya)
dosya.close()

# Çıktı almadık ancak üstteki kodlar sayesinde print() fonksiyonu, çıktılarını deneme.txt adlı bir dosyaya yazdırdı.

