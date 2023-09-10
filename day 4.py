with open("4.txt", encoding="utf-8") as fail:
    summa = 0
    for rida in fail:
        üks, kaks = rida.strip().split(",")
        üks1, üks2 = üks.split("-")
        kaks1, kaks2 = kaks.split("-")
        if int(üks1) >= int(kaks1) and int(üks2) <= int(kaks2) or int(üks1) <= int(kaks1) and int(üks2) >= int(kaks2):
            summa += 1
print(summa)


with open("4.txt", encoding="utf-8") as fail:
    summa = 0
    for rida in fail:
        üks, kaks = rida.strip().split(",")
        üks1, üks2 = [int(x) for x in üks.split("-")]
        kaks1, kaks2 = [int(x) for x in kaks.split("-")]

        if kaks1 <= üks1 <= kaks2  or kaks1 <= üks2 <= kaks2 or üks1 >= kaks1 and üks2 <= kaks2 or üks1 <= kaks1 and üks2 >= kaks2:
            summa += 1

print(summa)