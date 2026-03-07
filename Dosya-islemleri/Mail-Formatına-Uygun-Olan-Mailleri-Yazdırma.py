def bakalımbi(eleman):
    eleman = eleman.strip()
    if eleman[-10:] == "@gmail.com":
        print(eleman)
    else:
        print("{} ifadesi mail formatına uygun değil!".format(eleman))

with open("mailler.txt","r",encoding = "utf-8") as file:
    for i in file.readlines():
        bakalımbi(i)