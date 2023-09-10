with open("6.txt", encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        for i in range(len(rida)-14):
            kood = rida[i:i+14]
            if len(set(kood)) == len(kood):
                break
        print(i+14)