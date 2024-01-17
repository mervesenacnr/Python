print('Yarın Eskişehir\'e gidiyorum.')
print("\"book\" kelimesi Türkçede \"kitap\" anlamına gelir.")
print("Python programlama dilinin adı \"piton\" yılanından gelmez")
print("""İstanbul'un 5 günlük hava durumu tahmini""")
print("İstanbul'un 5 günlük hava durumu tahmini")
print('İstanbul\'un 5 günlük hava durumu tahmini')
"""
Bütün örneklerde \ işaretini kullandığımızı görüyorsunuz. 
İşte bu tür işaretlere Python’da kaçış dizisi (escape sequence) adı verilir. 
Bu işaretler karakter dizilerini tanımlarken oluşabilecek hatalardan kaçmamızı sağlar.
"""
print("Python 1990 yılında Guido Van Rossum \
tarafından geliştirilmeye başlanmış, oldukça \
güçlü ve yetenekli bir programlama dilidir.")
başlık = "Türkiye'de Özgür Yazılımın Geçmişi"
print(başlık, "\n", "-"*len(başlık), sep="")
başlık = "Alışveriş Listesi"
print(başlık, "\n", "-"*len(başlık), sep="")
print("bir", "iki", "üç", sep="\t")
print(*"123456789", sep="\t")
print("\a")
print("\a" * 10)
print("Merhaba\rZalim Dünya!")
print("Merhaba\rDünya")
"""
Burada, “Merhaba” karakter dizisi ekrana yazdırıldıktan sonra \r kaçış dizisinin etkisiyle satır başına dönülüyor
ve bu kaçış dizisinden sonra gelen “Dünya” karakter dizisi “Merhaba” karakter dizisinin üzerine yazıyor. 
Tabii “Dünya” karakter dizisi içinde 5 karakter, “Merhaba” karakter dizisi içinde ise 7 karakter olduğu için, “Merhaba”
karakter dizisinin son iki karakteri (“ba”) dışarda kalıyor. Böylece ortaya “Dünyaba” gibi bir şey çıkıyor.
"""
print("düşey\vsekme")
print("yahoo.com\b")
print("yahoo.com\b.uk")
print('istihza', '.', 'com', sep='')
print('istihza', '\b.', '\bcom')
print('istihza\b\b\bsna')
"""
UNICODE, karakterlerin, harflerin, sayıların ve bilgisayar ekranında gördüğümüz öteki bütün işaretlerin her 
biri için tek ve benzersiz bir numaranın tanımlandığı bir sistemdir. Bu sistemde, ‘kod konumu’ (code point) 
adı verilen bu numaralar özel bir şekilde gösterilir. Örneğin ‘ı’ harfi UNICODE sisteminde şu şekilde temsil edilir: u+0131
"""
print('\u0131')
print('\U00000131')
"""
U kaçış dizisinden sonra gelen kısım toplam 8 haneli bir sayıdan,
u kaçış dizisinde ise bu kısmı toplam 4 haneli bir sayıdan oluşuyor
"""
print("\x41")
print("\x4E")
"""
\.x kaçış dizisini kullanarak, onaltılı (hexadecimal) sayma sistemindeki bir sayının karakter
karşılığını gösterebilirsiniz.
"""
print("Kaçış dizileri: \, \n, \t, \a, \\, r")
print("Kaçış dizileri: \\, \\n, \\t, \\a, \\\, r")
print(r"Kaçış dizileri: \, \n, \t, \a, \\, r")
f = open("deneme.txt", "w")
print("deneme\fdeneme", file=f)
f.close()
