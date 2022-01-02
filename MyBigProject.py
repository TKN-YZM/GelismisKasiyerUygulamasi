import time #sleep fonksiyonu ile programımızı daha gerçekçi yapıyoruz
from datetime import  datetime #Saat ve dakika islemlerini gostermek icin

market_urunleri={"dondurma":7.50,"kola":8.95,"cipsi":5.45,"su":1.50,"çikolata":4.25,"mısır gevreği":7.95}
manav_urunleri={"elma":4.50,"mandalina":5.45,"portakal":5.95,"muz":12.45,"çilek":13.25}
kasap_urunleri={"kıyma":53.45,"kuşbaşı":65.25,"kasap köfte":53.90}


urun_listesi=[] #alinan ürünleri kaydettiğimiz yer
adet_listesi=[] #adetlerini de buraya kaydedicez
toplam_hesap=0 #alinan her ürününü fiyatının eklendiği yer

print("----------------KASIYER UYGULAMASI-------------------\n1-Market Urunleri\n2-Manav Urunleri\n3-Kasap Urunleri")
while True:
    secim=input("Lutfen Kategorilerden Birini Seciniz (Cikmak icin 'q' harfini tuslayiniz): ") #Kategori secimi yaptırıyoruz
    if secim=="1":
        print("Market Bolumune Hos Geldiniz.")
        while True:
            urun_ismi=input("Lutfen Market Urunlerinden Urun Ismini Giriniz: ").lower()
            print("Urunlerimiz: {}".format(market_urunleri))
            if urun_ismi in market_urunleri.keys():                                #Kullanıcının girdiği isim sözlükteki ürün ismiyle eşleşiyorsa
                adet=int(input("Lutfen adet giriniz: "))
                print("{} urunuden {} adet basariyla sepetinize eklenmistir".format(urun_ismi,adet))
                urun_listesi.append(urun_ismi)              #baştaki ürün listemize ekliyoruz
                adet_listesi.append(adet)                   #baştaki adet_listesine girilen adedi ekliyoruz
                toplam_hesap+=market_urunleri[urun_ismi]*adet   #
                print("Guncel Urun Listeniz: {}\nAdetleri: {}".format(urun_listesi,adet_listesi))
                print("Toplam ucretiniz: {}".format(round(toplam_hesap, 2)))
                print("Cikmak icin 'q' harfini tuslayabilirsiniz")

            elif urun_ismi=="q":
                print("Market Bolumunden Cikis Yapiliyor...")
                time.sleep(1)
                print("Almis Oldugunuz Urunler:{}\nAdetleri: {}".format(urun_listesi,adet_listesi))
                break
            else:
                print("Yanlis ürün girisi yapilmistir.Lutfen listeyi tekrar gözden geciriniz.")


    elif secim=="2":
        print("Manav Bolumune Hos Geldiniz")
        while True:
            print("Urunlerimiz: {}".format(manav_urunleri))
            urun_ismi=input("Lutfen Manav Bolumunden Urun Ismini Giriniz: ").lower()
            if urun_ismi in manav_urunleri.keys():
                adet=int(input("Lutfen kilogram giriniz: "))
                print("{} urunuden {} kilo basariyla sepetinize eklenmistir".format(urun_ismi,adet))
                urun_listesi.append(urun_ismi)
                adet_listesi.append(adet)
                toplam_hesap+=manav_urunleri[urun_ismi]*adet
                print("Guncel Urun Listeniz: {}\nAdetleri: {}".format(urun_listesi, adet_listesi))
                print("Toplam ucretiniz: {}".format(round(toplam_hesap, 2)))
                print("Cikmak icin 'q' harfini tuslayabilirsiniz")
            elif urun_ismi=="q":
                print("Manav Bolumunden Cikis Yapiliyor...")
                time.sleep(1)
                print("Almis Oldugunuz Urunler:{}\nAdetleri: {}".format(urun_listesi,adet_listesi))
                print("Toplam ucretiniz:{}".format(round(toplam_hesap,2)))
                break
            else:
                print("Yanlis ürün girisi yapilmistir.Lutfen listeyi tekrar gözden geciriniz.")

    elif secim =="3":
        print("Kasap Bolumune Hos Geldiniz.")
        while True:
            print("Urunlerimiz: {}".format(kasap_urunleri))
            urun_ismi = input("Lutfen Kasap Bolumunden  Urun Ismini Giriniz: ").lower()
            if urun_ismi in kasap_urunleri.keys():
                adet = int(input("Lutfen kilo giriniz: "))
                print("{} urunuden {} kilo basariyla sepetinize eklenmistir".format(urun_ismi, adet))
                urun_listesi.append(urun_ismi)
                adet_listesi.append(adet)
                toplam_hesap += kasap_urunleri[urun_ismi] * adet
                print("Guncel Urun Listeniz: {}\nAdetleri: {}".format(urun_listesi, adet_listesi))
                print("Toplam ucretiniz: {}".format(round(toplam_hesap, 2)))
                print("Cikmak icin 'q' harfini tuslayabilirsiniz")

            elif urun_ismi == "q":
                print("Kasap Bolumunden Cikis Yapiliyor...")
                time.sleep(1)
                print("Almis Oldugunuz Urunler:{}\nAdetleri: {}".format(urun_listesi, adet_listesi))
                print("Toplam ucretiniz: {}".format(round(toplam_hesap, 2)))
                break
            else:
                print("Yanlis ürün girisi yapilmistir.Lutfen listeyi tekrar gözden geciriniz.")


    elif secim=="q":
        print("Kasiyer Programindan Cikis Yapiliyor...")
        print("Toplam tutarınız: {}".format(round(toplam_hesap,2)))
        time.sleep(1)
        while True:
            print("Almis oldugunuz urunler: {}\nAdetleri: {}".format(urun_listesi, adet_listesi))
            evet_hayir=input("Iade etmek istediginiz urununuz varsa lutfen E/H yaziniz: ").upper()
            if evet_hayir=="E":
                silinecek_urun=input("Lutfen iade edilecek olan urunun ismini giriniz: ")
                if silinecek_urun in urun_listesi:
                    silinecek_adet=int(input("Lutfen iade edilecek urunun adetini giriniz: "))
                    urunun_indexi=urun_listesi.index(silinecek_urun)
                    indexteki_adet=adet_listesi[urunun_indexi]

                    if(indexteki_adet<silinecek_adet):
                        print("Almis oldugunuz urunden fazla iade islemi yapamazsınız.Lutfen tekrardan gozden geciriniz")
                    else:
                        print("{} urunundan {} adet basiryla silinmistir".format(silinecek_urun,silinecek_adet))
                        adet_listesi[urunun_indexi]=adet_listesi[urunun_indexi]-silinecek_adet
                        tum_urunler={"dondurma":7.50,"kola":8.95,"cipsi":5.45,"su":1.50,"çikolata":4.25,"mısır gevreği":7.95,"elma":4.50,"mandalina":5.45,"portakal":5.95,"muz":12.45,"çilek":13.25,"kıyma":53.45,"kuşbaşı":65.25,"kasap köfte":53.90}
                        toplam_hesap-=tum_urunler[silinecek_urun]*silinecek_adet
                        print("Almis oldugunuz urunleriniz: {}\nAdetleri: {}".format(urun_listesi,adet_listesi))
                        print("Toplam ucretiniz: {}".format(round(toplam_hesap, 2)))

            elif evet_hayir=="H":
                print("Bizi tercih ettiginiz icin tesekkur ederiz")
                print("Cikis yapiliyor....")
                print("\n-------------------------TKN MARKET-----------------------\n")
                print("Islem Saati: {}".format(datetime.now().strftime("%H:%M")))
                print("Urun Listeniz: {}\nAdetleri: {}".format(urun_listesi,adet_listesi))
                print("Toplam Tutariniz: {}".format(round(toplam_hesap, 2)))
                time.sleep(1)
                break

            elif evet_hayir=="Q":
                print("Bizi tercih ettiginiz icin tesekkur ederiz")
                print("Cikis yapiliyor....")
                print("\n-------------------------TKN MARKET-----------------------\n")
                print("Islem Saati: {}".format(datetime.now().strftime("%H:%M")))
                print("Urun Listeniz: {}\nAdetleri: {}".format(urun_listesi, adet_listesi))
                print("Toplam Tutariniz: {}".format(round(toplam_hesap, 2)))
                time.sleep(1)
                break

            else:
                print("Yanlis veri girisi yaptiniz.Lutfen sadece E/H yazin.Girdiginiz veri: {}".format(evet_hayir))

        break

    else:
        print("Yanlis katolog girisi yapılmıstır.Lutfen katolog numarasını giriniz: ")