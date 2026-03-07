def yazdır(satır):
    satır = satır.strip()
    digerliste = []
    digerliste = satır.split(",")
    return digerliste

try:
    with open("Futbolcular.txt", "r", encoding="utf-8") as file:
        bosliste = []
        for i in file:
            gelen_veri = yazdır(i)
            bosliste.append(gelen_veri)
        print(bosliste)
except FileNotFoundError:
    print("Dosyada eleman yok")
FutbolcularFB = []
for i in bosliste:
    if (i[1] == "Fenerbahçe"):
        FutbolcularFB.append(i[0])
        FutbolcularFB.append("\n")
with open("FutbolcularFB.txt","w",encoding="utf-8") as file2:
    for i in FutbolcularFB:
        file2.write(i)
FutbolcularGS = []
for i in bosliste:
    if i[1] == "Galatasaray":
        FutbolcularGS.append(i[0])
        FutbolcularGS.append("\n")
with open("FutbolcularGS.txt","w",encoding="utf-8") as file3:
    for i in FutbolcularGS:
        file3.write(i)
FutbolcularBJK = []
for i in bosliste:
    if i[1] == "Beşiktaş":
        FutbolcularBJK.append(i[0])
        FutbolcularBJK.append("\n")
with open("FutbolcularBJK.txt","w",encoding="utf-8") as file4:
    for i in FutbolcularBJK:
        file4.write(i)






