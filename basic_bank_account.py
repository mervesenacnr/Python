print("""
_____▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄_
─────█▒▒░░░░░░░░░▒▒█───
──────█░░█░░░░░█░░█────
───▄▄──█░░░▀█▀░░░█──▄▄─
──█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█----╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗-----█
█----║║║╠─║─║─║║║║║╠─-----█
█----╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝-----█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

Ayicik Banka Hesabına hoş geldiniz !
────────────────────────────────────""")

giris = """
°ºO•❤•.¸✿¸.•❤• 1) Banka Hesabı Oluştur
°ºO•❤•.¸✿¸.•❤• 2) Banka Hesabına Giriş Yap
°ºO•❤•.¸✿¸.•❤• q) Çıkış
"""
print(giris)

anahtar = 1
islem = 1
kullanici_adi = " "
sifre = 0
yeni_kullanici_adi = " "
yeni_sifre = 0

while anahtar == 1:
    soru = input("Lütfen yapılacak işlemi seçiniz: ")
    if soru == "q":
        print("Çıkış yapılıyor...")
        exit()
    elif soru == "1":
        yeni_kullanici_adi = str(input("Lütfen kullanici adinizi oluşturunuz:"))
        yeni_sifre = int(input("Lütfen sifrenizi olusturunuz:"))
        print("Yeni hesap bilgileriniz:\n", "Kullanici adi: ", yeni_kullanici_adi, "\n", "Sifre: ", yeni_sifre, sep="")
    elif soru == "2":
        print("Lütfen hesap bilgilerinizi giriniz...")
        kullanici_adi = str(input("Kullanici adi:"))
        sifre = int(input("Sifre:"))

        if kullanici_adi == yeni_kullanici_adi and sifre == yeni_sifre:
            print("Hesabınıza giriş yaptınız ", kullanici_adi, ".", sep="")
            bakiye = 0
            yukleme = 0
            cekme = 0
            while islem == 1:

                print("°ºO•❤•.¸✿¸.•❤• 1) Para Yükle", "°ºO•❤•.¸✿¸.•❤• 2) Para Çek", "°ºO•❤•.¸✿¸.•❤• q) Çıkış", sep="\n")
                ikinci_soru = input("Lütfen yapılacak işlemi seçiniz: ")

                if ikinci_soru == "q":
                    print("Çıkış yapılıyor...")
                    exit()
                elif ikinci_soru == "1":
                    yukleme = int(input("Lütfen yüklemek istediğiniz para tutarını giriniz: "))
                    bakiye += yukleme
                    print("Yeni bakiyeniz: ", bakiye, "TL", sep="")
                elif ikinci_soru == "2":
                    cekme = int(input("Lütfen cekmek istediğiniz para tutarını giriniz: "))
                    if cekme <= bakiye:
                        bakiye -= cekme
                        print("Yeni bakiyeniz: ", bakiye, "TL", sep="")
                    else:
                        print("Yetersiz bakiye. Cekme işlemi gerçekleştirilemedi.")
        elif kullanici_adi != yeni_kullanici_adi and sifre == yeni_sifre:
            print("Hatali kullanici adi girdiniz lütfen tekrar deneyiniz...")
        elif kullanici_adi == yeni_kullanici_adi and sifre != yeni_sifre:
            print("Hatali sifre girdiniz lütfen tekrar deneyiniz...")
        elif kullanici_adi != yeni_kullanici_adi and sifre != yeni_sifre:
            print("Hatali kullanici adi veya sifre girdiniz lütfen tekrar deneyiniz...")