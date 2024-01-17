"""
1-Cumartesi-Pazar günleri çalışmıyoruz.
2-Dolayısıyla ayda X gün çalışıyoruz.
3-Evden işe gitmek için kullandığımız vasıtanın ücreti 8.5 TL
4-İşten eve dönmek için kullandığımız vasıtanın ücreti 9.5 TL
Elimizdeki bu verilere dayanarak yol masrafı hesaplayan bir uygulama tasarlayacağız.
Denklem:
aylık yol masrafı = gün x ( gidişTL + dönüşTL )
aylık yol masrafı = X x ( 8.5 TL + 9.5 TL )
"""

print("""
 -----------------------------------------------------------------------------------------------------
| ‘°ºø•❤•.¸✿¸.•❤•.❀•. (AYLIK YOL MASRAFI HESAPLAMA UYGULAMASINA HOŞ GELDİNİZ ) .•❀.•❤•.¸✿¸.•❤•øº°‘|
 -----------------------------------------------------------------------------------------------------
""")
isim = ""
soy_isim = ""
gün = 0
isim = str(input("Adınız nedir?"))
soy_isim = str(input("Soy adınız nedir?"))
gün = int(input("Bir ayda kaç gün işe gidiyorsunuz?"))
aylik_yol_masrafi = gün * 18
print("-"*30)
print("İsim               \t:", isim)
print("Soy isim        \t:", soy_isim)
print("Çalışılan gün sayısı:", gün)
print("İşe gidiş ücreti\t:", "8.5TL")
print("İşten dönüş ücreti\t:", "9.5TL")
print("-"*30)
print("AYLIK YOL MASRAFI\t:", aylik_yol_masrafi, "TL")



