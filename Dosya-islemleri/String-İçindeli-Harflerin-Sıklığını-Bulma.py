string1 = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekansOfString1 = dict()
for i in string1:
    if i in frekansOfString1:
        frekansOfString1[i] += 1
    else:
        frekansOfString1[i] = 1
for i,j in frekansOfString1.items():
    print("{} harfi stringte {} defa geçmektedir".format(i,j))