#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
result = True
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not(x or y or z)) == (not x and not y and not z):
                continue
            else:
                result = False

if result == True:
    print("Утверждение истинно!")
else:
    print("Утверждение ложно!")
