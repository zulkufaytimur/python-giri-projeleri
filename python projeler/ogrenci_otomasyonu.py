print("------------->>> OGRENCİ OTOMASYONU <<<---------------")
ders_kaydı = []
ogrenciler = []

while True:
    print(
        """
        1. Öğrenci Girişi
        2. Öğretmen Girişi
        """
    )
    işlem = input("Lütfen bir işlem seçiniz: ")

    if işlem == '1':  # Öğrenci Girişi
        ogr_ad = input("Lütfen adınızı giriniz: ")
        ogr_no = int(input("Lütfen öğrenci numaranızı giriniz: "))
        print(f"Hoşgeldiniz, {ogr_ad}!")

        while True:
            print(
                """
                1. Ders Kaydı
                2. Not Hesaplama
                3. Çıkış
                """
            )
            işlem = input("Lütfen bir işlem seçiniz: ")

            if işlem == '1':  # Ders Kaydı
                ders_ad = input("Lütfen ders adı giriniz: ")
                ders_kaydı.append({"ogr_no": ogr_no, "ogr_ad": ogr_ad, "ders": ders_ad})
                print(f"{ders_ad} başarıyla kaydedildi!")

            elif işlem == '2':  # Not Hesaplama
                vize = float(input("Vize notunuzu giriniz: "))
                final = float(input("Final notunuzu giriniz: "))
                ortalama = (vize * 0.4) + (final * 0.6)
                print(f"Ders notu ortalamanız: {ortalama:.2f}")
                if ortalama >= 60:
                    print("Tebrikler, dersi geçtiniz!")
                else:
                    print("Maalesef, dersten kaldınız.")

            elif işlem == '3':  # Çıkış
                print("Başarılı bir şekilde çıkış yapıldı...")
                break

            else:
                print("Geçersiz bir işlem yaptınız...")

    elif işlem == '2':  # Öğretmen Girişi
        ogretmen_ad = input("Lütfen adınızı giriniz: ")
        ogretmen_id = int(input("Lütfen öğretmen numaranızı giriniz: "))
        print(f"Hoşgeldiniz, {ogretmen_ad}!")

        while True:
            print(
                """
                1. Öğrenci Ekleme
                2. Öğrenci Silme
                3. Öğrenci Sorgulama
                4. Öğrenci Listesi
                5. Ders Listesi
                6. Çıkış
                """
            )
            islem = input("Lütfen bir işlem seçiniz: ")

            if islem == '1':  # Öğrenci Ekleme
                ogr_ad = input("Öğrenci adını giriniz: ")
                ogr_soyad = input("Öğrenci soyadını giriniz: ")
                ogr_no = int(input("Lütfen öğrenci numarasını giriniz: "))
                ogrenciler.append({"ogrenci_no": ogr_no, "ogr_ad": ogr_ad, "ogr_soyad": ogr_soyad})
                print(f"{ogr_ad} başarıyla listeye eklendi!")

            elif islem == '2':  # Öğrenci Silme
                ogr_no = int(input("Silmek istediğiniz öğrenci numarasını giriniz: "))
                ogrenciler = [ogr for ogr in ogrenciler if ogr["ogrenci_no"] != ogr_no]
                print("Öğrenci başarıyla silindi!")

            elif islem == '3':  # Öğrenci Sorgulama
                sorgu_no = int(input("Sorgulamak istediğiniz öğrenci numarasını giriniz: "))
                ogrenci_bulundu = False
                for ogrenci in ogrenciler:
                    if ogrenci["ogrenci_no"] == sorgu_no:
                        print(f"Öğrenci Adı: {ogrenci['ogr_ad']}, Soyadı: {ogrenci['ogr_soyad']}, Numara: {ogrenci['ogrenci_no']}")
                        ogrenci_bulundu = True
                        break
                if not ogrenci_bulundu:
                    print("Bu numarayla kayıtlı öğrenci bulunamadı.")

            elif islem == '4':  # Öğrenci Listesi
                if not ogrenciler:
                    print("Henüz öğrenci kaydı bulunmuyor.")
                else:
                    print("Öğrenci Listesi:")
                    for ogrenci in ogrenciler:
                        print(f"Ad: {ogrenci['ogr_ad']}, Soyad: {ogrenci['ogr_soyad']}, Numara: {ogrenci['ogrenci_no']}")

            elif islem == '5':  # Ders Listesi
                if not ders_kaydı:
                    print("Henüz ders kaydı bulunmuyor.")
                else:
                    print("Ders Listesi:")
                    for ders in ders_kaydı:
                        print(f"Öğrenci Adı: {ders['ogr_ad']}, Ders: {ders['ders']}")

            elif islem == '6':  # Çıkış
                print("Öğretmen menüsünden çıkış yapılıyor...")
                break

            else:
                print("Geçersiz işlem, tekrar deneyin.")

    else:
        print("Geçersiz işlem, lütfen tekrar deneyin.")

                