with open("input.txt", encoding = "utf-8") as fail:
    maksimum = 0
    summa = 0
    for rida in fail:
        rida = rida.strip()
        if rida == '':
            if maksimum < summa:
                maksimum = summa
            summa = 0

        else:
            summa += int(rida)

print(maksimum)

with open("input.txt", encoding = "utf-8") as fail:

    järjend = []
    summa = 0
    for rida in fail:
        rida = rida.strip()
        if rida == '':
            järjend.append(summa)
            summa = 0

        else:
            summa += int(rida)

sorteeritud = sorted(järjend)  

print(sum(sorteeritud[-3:]))