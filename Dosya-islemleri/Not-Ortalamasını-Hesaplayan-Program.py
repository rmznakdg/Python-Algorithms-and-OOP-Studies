def not_hesapla(satır):
    satır = satır.strip()
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    ortalama = not1*(3/10) + not2*(3/10) + not3*(4/10)
    if ortalama>=90:
        harf_notu= "AA"
    elif ortalama>=80:
        harf_notu="BA"
    elif ortalama>=70:
        harf_notu="BB"
    elif ortalama>=65:
        harf_notu="CB"
    elif ortalama>=55:
        harf_notu="CC"
    elif ortalama>=50:
        harf_notu="DC"
    elif ortalama>=45:
        harf_notu="DD"
    else:
        harf_notu="FF"

    return f"{isim} -------> {harf_notu} \n"

with open("NotlarSınavDeneme.txt", "r", encoding ="utf+8") as file:
    yeni_liste = []
    for i in file:
        yeni_liste.append(not_hesapla(i))
    with open("NotlarYazılanDosyaDeneme.txt", "w", encoding="utf-8") as file2:
        for i in yeni_liste:
            file2.write(i)
with open("NotlarYazılanDosyaDeneme.txt","r", encoding="utf-8") as file3:
    KalanlarListesi = []
    for i in file3:
        if i.strip()[-2:]=="FF":
            KalanlarListesi.append(i)
    with open("KalanlarListesi.txt","w",encoding = "utf-8") as file4:
        for i in KalanlarListesi:
            file4.write(i)



