def ilkHarf(eleman):
    elaman = eleman.strip()
    print(eleman[0])

with open("şiir.txt","r", encoding = "utf-8") as file:
    for i in file.readlines():
        ilkHarf(i)
