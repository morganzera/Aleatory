m = 44.045 # media
i = [44.40, # lista de valores
    44.30,
    44.20,
    44.10,
    44.10,
    44.00,
    43.95,
    43.90,
    43.90,
    43.60]
b = []
sup = 0
for x in i:
    sub = (x - m)**2
    b.append(sub)
for x in b:
    sup += x
dp = (sup/(len(i)*(len(i)-1)))**(1/2)
print(dp)
