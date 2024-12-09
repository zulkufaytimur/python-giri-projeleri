print("*************\nATM Sistemine Hoşgeldiniz****************")

bakiye = 1000
kullanici_ad = "admin"
sifre = "admin"
hesap_hareketleri = []  # Hesap hareketlerini saklamak için liste

while True:
    girilen_kullanici_ad = input("Lütfen kullanıcı adınızı giriniz: ")
    girilen_sifre = input("Lütfen şifrenizi giriniz: ")
    
    if girilen_kullanici_ad == kullanici_ad and girilen_sifre == sifre:
        print("Başarılı giriş yaptınız!")
        while True:
            print(
                """
                1. Bakiye Sorgulama
                2. Para Yatırma
                3. Para Çekme
                4. Hesap Hareketleri
                5. Çıkış Yap
                """
            )
            islem = input("Lütfen bir işlem seçiniz: ")
            
            if islem == "1":
                print("Bakiyeniz {} TL'dir.".format(bakiye))
            
            elif islem == "2":
                miktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
                bakiye += miktar
                hesap_hareketleri.append(f"Para Yatırma: +{miktar} TL | Güncel Bakiye: {bakiye} TL")
                print("Başarılı! Yeni bakiyeniz: {} TL".format(bakiye))
            
            elif islem == "3":
                miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
                if bakiye >= miktar:
                    bakiye -= miktar
                    hesap_hareketleri.append(f"Para Çekme: -{miktar} TL | Güncel Bakiye: {bakiye} TL")
                    print("Başarılı! Kalan bakiyeniz: {} TL".format(bakiye))
                else:
                    print("Yetersiz bakiye! Mevcut bakiyeniz: {} TL".format(bakiye))
            
            elif islem == "4":
                print("Hesap Hareketleriniz:")
                if hesap_hareketleri:
                    for hareket in hesap_hareketleri:
                        print(hareket)
                else:
                    print("Henüz bir hareket bulunmamaktadır.")
            
            elif islem == "5":
                print("Çıkış yapılıyor. Yine bekleriz!")
                break
            
            else:
                print("Lütfen geçerli bir işlem numarası giriniz!")
        
        break  # Doğru girişten sonra dış döngüyü sonlandırır.

    else:
        print("HATA: Kullanıcı adı veya şifre yanlış! Lütfen tekrar deneyin.")

