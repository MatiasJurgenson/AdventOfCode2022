A, X = 1, 1
B, Y = 2, 2
C, Z = 3, 3

with open("input2.txt", encoding = "utf-8") as fail:
    summa = 0
    for rida in fail:
        vastane, sina = rida.strip().split(" ")
        # valiku summa liitimine
        if sina == "X":
            summa += 1
        elif sina == "Y":
            summa += 2
        elif sina == "Z":
            summa += 3

        #viik, võit

        if vastane == "A" and sina == "X" or vastane == "B" and sina == "Y" or vastane == "C" and sina == "Z":
            summa += 3
        elif vastane == "A" and sina == "Y" or vastane == "B" and sina == "Z" or vastane == "C" and sina == "X":
            summa += 6
            
print(summa)

#X lose Y draw Z win

with open("input2.txt", encoding="utf-8") as fail:
    summa = 0
    for rida in fail:
        vastane, sina = rida.strip().split(" ")
        
        if sina == "Y":
            summa += 3
            if vastane == "A":
                summa += 1
            elif vastane == "B":
                summa += 2
            elif vastane == "C":
                summa += 3

        elif sina == "Z":
            summa += 6
            if vastane == "A":
                summa += 2
            elif vastane == "B":
                summa += 3
            elif vastane == "C":
                summa += 1

        else:
            if vastane == "A":
                summa += 3
            elif vastane == "B":
                summa += 1
            elif vastane == "C":
                summa += 2

print(summa)
            

