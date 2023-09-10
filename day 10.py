tsüklid = [20, 60, 100, 140, 180, 220]

rida1 = ''
rida2 = ''
rida3 = ''
rida4 = ''
rida5 = ''
rida6 = ''



with open("10.txt", encoding="utf-8") as fail:
    summa = 0
    liida = 0
    i = 0
    x = 1

    read = fail.readlines()
    for rida in read:
        try:
            käsk, kogus = rida.strip().split(" ")

        except:
            käsk = rida.strip()

        if liida == 2:
            liida = 0
            x += liidetav_kogus

        if käsk == "noop":
            i += 1
            if i in tsüklid:
                summa += i*x

        else:
            for j in range(2):
                i += 1
                liida += 1
                liidetav_kogus = int(kogus)
                if i in tsüklid:
                    summa += i*x

print(summa)


with open("10.txt", encoding="utf-8") as fail:
    summa = 0
    liida = 0
    i = 0
    x = 1

    read = fail.readlines()
    for rida in read:
        try:
            käsk, kogus = rida.strip().split(" ")

        except:
            käsk = rida.strip()

        if liida == 2:
            liida = 0
            x += liidetav_kogus

        if käsk == "noop":
            i += 1
            if i <= 40:
                if x <= i <= x+2:
                    rida1 += '#'
                else:
                    rida1 += '.'
            elif i <= 80:
                if x <= i-40 <= x+2:
                    rida2 += '#'
                else:
                    rida2 += '.'
            elif i <= 120:
                if x <= i-80 <= x+2:
                    rida3 += '#'
                else:
                    rida3 += '.'
            elif i <= 160:
                if x <= i-120 <= x+2:
                    rida4 += '#'
                else:
                    rida4 += '.'
            elif i <= 200:
                if x <= i-160 <= x+2:
                    rida5 += '#'
                else:
                    rida5 += '.'
            else:
                if x <= i-200 <= x+2:
                    rida6 += '#'
                else:
                    rida6 += '.'




        else:
            for j in range(2):
                i += 1
                liida += 1
                liidetav_kogus = int(kogus)
                if i <= 40:
                    if x <= i <= x+2:
                        rida1 += '#'
                    else:
                        rida1 += '.'
                elif i <= 80:
                    if x <= i-40 <= x+2:
                        rida2 += '#'
                    else:
                        rida2 += '.'
                elif i <= 120:
                    if x <= i-80 <= x+2:
                        rida3 += '#'
                    else:
                        rida3 += '.'
                elif i <= 160:
                    if x <= i-120 <= x+2:
                        rida4 += '#'
                    else:
                        rida4 += '.'
                elif i <= 200:
                    if x <= i-160 <= x+2:
                        rida5 += '#'
                    else:
                        rida5 += '.'
                else:
                    if x <= i-200 <= x+2:
                        rida6 += '#'
                    else:
                        rida6 += '.'

ridad = [rida1,rida2,rida3,rida4,rida5,rida6]
for asi in ridad:
    print(asi)
        

        

