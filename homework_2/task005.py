#Реализуйте алгоритм перемешивания списка.

import random

num_list = [random.randint(0, 100) for i in range(9)]
print(num_list)
random.shuffle(num_list)
print(num_list)