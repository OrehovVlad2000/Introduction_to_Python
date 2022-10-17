#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    if result == False:
        break
    for y in range(2):
        if result == False:
            break
        for z in range(2):
            if (not(x or y or z)) == (not x and not y and not z):
                result = True
            else:
                result = False
                break

if result == True:
    print("Утверждение истинно!")
else:
    print("Утверждение ложно!")
