priority = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("3.txt", encoding="utf-8") as fail:
    järjend = []
    for rida in fail:
        andmed = rida.strip()
        pikkus = int(len(andmed)/2) 
        #print(andmed[:pikkus])
        #print(andmed[pikkus:])
        for i in andmed[pikkus:]:
            for j in andmed[:pikkus]:
                if i == j:
                    järjend.append(i)
                    break
            else:
                continue
            break
                    
summa = 0   
for täht in järjend:
    summa += (priority.index(täht))



with open("3.txt", encoding="utf-8") as fail:
    järjend = []
    read = fail.readlines()
    for i in range(0, len(read), 3):
        for j in read[i]:
            if j in read[i+1] and j in read[i+2] and j != '\n': #and j not in järjend 
                järjend.append(j)
                break

summa = 0   
for täht in järjend:
    summa += (priority.index(täht))

print(summa)
