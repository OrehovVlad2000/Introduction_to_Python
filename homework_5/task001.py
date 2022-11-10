# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

text = "Научная фантастика может быть полезной — она стимулирует воображение и избавляет от страха перед будущим."
text = text.split()
print(text)
result_text = []
for i in range(len(text)):
    if "а" in text[i].lower() and "б" in text[i].lower() and "в" in text[i].lower():
        continue
    else:
        result_text.append(text[i])

text = " ".join(result_text)
print(result_text)