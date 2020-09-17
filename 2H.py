# На экскурсии в музее связи кадеты узнали о различных способах шифрования данных, в том числе криптографических алгоритмах. 
# Кадеты Петров и Пупкин большие любители точных наук, в особенности математики, поэтому их заинтересовал алгоритм RSA, 
# основанный на работе с простыми числами. Вернувшись в расположение, они решили разработать свои открытый и закрытый ключи и 
# обмениваться зашифрованными сообщениями. Для их изготовления необходима пара простых чисел, а точнее произведение простых чисел из промежутке от M до N.

# Напишите программу, определяющую количество комбинаций, из которых ребята могут выбрать число для своего открытого и закрытого ключа.
# Под комбинацией понимается произведение двух различных простых чисел из промежутке от от M до N (порядок чисел в произведении не имеет значения).

# Входные данные:
# На вход программа получает два целых числа M и N - границы числового промежутка из которого выбираются простые числа (1<M, N≤105)

# Выходные данные:
# одно число - количество возможных комбинаций

# Sample Input 1:
# 19 28
# Sample Output 1:
# 1
# Sample Input 2:
# 22 48
# Sample Output 2:
# 21
