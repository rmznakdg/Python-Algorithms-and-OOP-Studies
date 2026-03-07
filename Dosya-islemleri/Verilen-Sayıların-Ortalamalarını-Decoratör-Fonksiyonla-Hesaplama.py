def ekstra(func):
    def wrapper(sayılar):
        tek_sayılar_toplamı = 0
        tek_sayı_sayacı = 0
        çift_sayılar_toplamı = 0
        çift_sayılar_sayacı = 0

        for sayı in sayılar:
            if (sayı % 2 == 0):
                çift_sayılar_sayacı+=1
                çift_sayılar_toplamı+=sayı
            else:
                tek_sayı_sayacı+=1
                tek_sayılar_toplamı+=sayı
        print("Tek sayılar adedi:", tek_sayı_sayacı)
        print("Tek sayıların ortalaması:", tek_sayılar_toplamı/tek_sayı_sayacı)
        print("Çift sayı adedi:", çift_sayılar_sayacı)
        print("Çift sayılar toplamı:",çift_sayılar_toplamı/çift_sayılar_sayacı)
        func(sayılar)
    return wrapper

@ekstra
def ortalama_hesapla(sayılar):
    toplam = 0
    for sayı in sayılar:
        toplam += sayı
    print("Ortalama:",toplam/len(sayılar))
ortalama_hesapla([2,6,8,9,15,685,3,-4])