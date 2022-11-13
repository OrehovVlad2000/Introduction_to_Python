# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('source_text.txt', 'w') as file:
    file.write('AAAAAAAAAAAAAAA55 fffffff')

with open('source_text.txt', 'r') as file:
    data = file.readline()


encoding = ''
prev_elem = ''
count = 1

if not data:
    print('Кодировать нечего!')

for each in data:
    if each != prev_elem:
        if prev_elem:
            if count > 9:
                temp = count
                while temp > 0:
                    encoding += f'{9 if temp > 9 else temp}{prev_elem}'
                    temp -= 9
            else:
                encoding += f'{count}{prev_elem}'
        count = 1
        prev_elem = each
    else:
        count += 1
else:
    encoding += str(count) + prev_elem
    with open('encoding.txt', 'w') as f_encode:
        f_encode.write(encoding)

with open('encoding.txt', 'r') as txt_encode:
    encoded_data = txt_encode.readline()
decoding = ''
counter = ''
prev = ''

for each in encoded_data:
    if each.isdigit():
        if prev.isdigit():
            decoding += each * int(counter)
            prev = ''
            counter = ''
        else:
            counter += each
            prev = each
    else:
        decoding += each * int(counter)
        counter = ''
        prev = ''

with open('decoding.txt', 'w') as txt_decode:
    txt_decode.write(decoding)
