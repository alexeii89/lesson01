#Название, годовая прибыль
Comp = {"Рога и копыта": 5000,
            "Рога": 6000,
            "Копыта": 3000,
            "Компания1": 785000,
            "Компания2": 8000,
            "Компания3": 33000,
            "Компания4": 98000,
            "Компания5": 23000
           }
#O(log n)
rez = sorted(Comp.items(), key=lambda x: x[1], reverse=True)
for i in rez[0:3]:
    print(i)


#N**2
rez = []
company = Comp
c = 0
while len(rez) != 3: #O(1)
    for i in company:#O(n)
        r = True
        for j in company:#O(n)
            if company[i] < company[j]:
                r = False
        if r == True:
            rez.append(i)
            company.pop(i)
            break
print(rez)