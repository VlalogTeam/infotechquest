# Дежурство по автопарку
# Кадеты в увольнении ходили в кино смотреть детективный фильм. В основе сюжета лежит история 
# проникновения солдат вражеского войска на территорию контрольно-технического пункта (КТП) 
# автопарка военной части и похищение оружия. Кадеты Петров и Пупкин достаточно практичные 
# и считают, что ошибок лучше не допускать, чем их потом исправлять, поэтому они решили найти ответ на вопрос: 
# как возможно было избежать проникновения врага и хищения оружия. Они внимательно изучили обязанности дежурного 
# по автопарку, согласно которым, он следит за сохранностью имущества и военной техники, находящейся под его 
# охраной. Для этого он фиксирует все въезжающие и выезжающие автомобили. Машины, которые выезжали и въехали 
# обратно в автопарк - встают на свои прежние места (если автомобиль въехал впервые, то он встает в конец ряда - 
# место, не принадлежащее никакому из выехавших автомобилей).

# В ходе дежурства ведется журнал передвижения транспортного средства, где фиксируются номера въезжающих и 
# выезжающих автомобилей. По истечению дежурства необходимо подать рапорт со сведениями о находящихся в автопарке
#  автомобилях. Кадеты решили, что если автоматизировать этот процесс, то неприятностей, описанных в сюжете, можно
#  избежать. Напишите программу учета въезда/выезда автомобилей. При вводе неверной комбинации Номер автомобиля + 
# команда (при попытке выезда автомобиля, отсутствующего в автопарке либо при въезде автомобиля уже находящегося в автопарке) 
# программа выводит сообщение об ошибке ERROR. Работа автопарка прекращается, начинается сверка автомобилей, перепроверка журнала.

# Входные данные:
# в первой строке вводится натуральное число N – количество автомобилей в автопарке (0< N ≤ 106)
# в каждой из N последующих строк подаются номера автомобилей, находящихся в автопарке; далее в последующих n 
# строках вводится код команды и через пробел номер автомобиля, выполняющего данную команду 
# (код команд in - въезд, out - выезд, delivery – сдача наряда), ввод заканчивается командой delivery, 
# но количество команд не превышает 105. Номера автомобилей - натуральные числа, не превышающие 106.

# Выходные данные:
# Программа выводит перечень номеров автомобилей, находящихся в автопарке на момент окончания дежурства курсанта.

# Sample Input 1:
# 5
# 27
# 56
# 28
# 77
# 48
# out 27
# out 77
# in 44
# out 28
# delivery
# Sample Output 1:
# 56
# 48
# 44
# Sample Input 2:
# 3
# 27
# 56
# 28
# out 27
# in 44
# in 27
# delivery
# Sample Output 2:
# 27
# 56
# 28
# 44
# Sample Input 3:
# 3
# 27
# 56
# 28
# in 89
# out 77
# delivery
# Sample Output 3:
# ERROR
# Time Limit: 15 секунд
# Memory Limit: 256 MB

cars = {}

for i in range(0, int(input())):
    cars[int(input())] = True

while True:
    inpstring = input()
    try:
        command, number = map(str, inpstring.split(" "))
        number = int(number)
        if command == "in":
            try:
                if cars[number]:
                    print("ERROR")
                    break
                else:
                    cars[number] = True
            except:
                cars[number] = True
        if command == "out":
            try:
                if cars[number]:
                    cars[number] = False
                else:
                    print("ERROR")
                    break
            except:
                print("ERROR")
                break
    except:
        if inpstring == "delivery":
            for element in cars.keys():
                if cars[element] == True:
                    print(element)
            break
            