with open("input8.txt", encoding="utf-8") as fail:
    nähtavad = 0

    read = fail.readlines()
    for i in range(len(read)):
        rida = read[i].strip()

        if i == 0 or i == len(read) - 1:
            nähtavad += len(rida)
        
        else:
            for number1, puu1 in enumerate(rida):
                mittenähtav = 0
                if number1 == 0 or number1 == len(read) - 1:
                    nähtavad += 1

                else:

                    for j in range(len(read)):
                        if j < i:
                            if int(read[j][number1]) >= int(puu1):
                                mittenähtav += 1
                                break
                    
                    for j in range(len(read)):
                        if j > i:
                            if int(read[j][number1]) >= int(puu1):
                                mittenähtav += 1
                                break

                    for number2, puu2 in enumerate(rida):
                        if number2 < number1:
                            if int(puu2) >= int(puu1):
                                mittenähtav += 1
                                break

                    for number2, puu2 in enumerate(rida):
                        if number2 > number1:
                            if int(puu2) >= int(puu1):
                                mittenähtav += 1
                                break

                    

                    if mittenähtav != 4:
                        nähtavad += 1

print(nähtavad)

with open("input8.txt", encoding="utf-8") as fail:
    suurim = 0

    read = fail.readlines()
    for i in range(len(read)):
        rida = read[i].strip()

        for number1, puu1 in enumerate(rida):
            nähtav_üles = 0
            nähtav_alla = 0
            nähtav_paremale = 0
            nähtav_vasakule = 0
            rida = read[i].strip()

            for j in reversed(range(len(read))):
                if j < i:
                    if int(read[j][number1]) < int(puu1):
                        nähtav_üles += 1
                    elif int(read[j][number1]) >= int(puu1):
                        nähtav_üles += 1
                        break
                        
            for j in range(len(read)):
                if j > i:
                    if int(read[j][number1]) < int(puu1):
                        nähtav_alla += 1
                    elif int(read[j][number1]) >= int(puu1):
                        nähtav_alla += 1
                        break
                        
            for j in reversed(range(len(rida))):
                if j < number1:
                    if int(rida[j]) < int(puu1):
                        nähtav_vasakule += 1

                    elif int(rida[j]) >= int(puu1):
                        nähtav_vasakule += 1
                        break

            for j in range(len(rida)):
                if j > number1:
                    if int(rida[j]) < int(puu1):
                        nähtav_paremale += 1

                    elif int(rida[j]) >= int(puu1):
                        nähtav_paremale += 1
                        break
            summa = nähtav_alla * nähtav_paremale * nähtav_vasakule * nähtav_üles
            if summa > suurim:
                suurim = summa

print(suurim)



                        
                    

                

        