def hesapla(satır):
    satır = satır.strip()
    yeniListe = satır.split(",")
    isimsoyisim = yeniListe[0]
    not1 = int(yeniListe[1])
    not2 = int(yeniListe[2])
    not3 = int(yeniListe[3])
    ortalama = float(not1*2/10 + not2*2/10 + not3*6/10)
    ortalama = round(ortalama,2)
    return (isimsoyisim,ortalama)

with open("Notlar.txt","r",encoding="utf-8") as file:
    NotListesi = []
    for i in file:
        gelenveri = hesapla(i)
        NotListesi.append(gelenveri)
for i in NotListesi:
    print(i)
max = 0
for i,j in NotListesi:
    if j > max:
        max = j
        isim = i
print("En yüksek ortalamaya sahip kişi: {} ve notu:{}".format(isim,max))

toplam = 0
for i,j in NotListesi:
    toplam+=j
    sınıfort = round(toplam/len(NotListesi),2)
print("Sınıf ortalaması: {}".format(sınıfort))

basarılıÖgrenciler = []
for i,j in NotListesi:
    if j>=85:
        basarılıÖgrenciler.append(i)
print("Başarılı Öğrenciler Listesi: ", basarılıÖgrenciler)

