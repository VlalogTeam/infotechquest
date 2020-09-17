def convert_value_to_mm(value, unit):
    value = int(value)
    unit = str(unit)
    if unit == "d":
        return value*25.4
    elif unit =="v":
        return value*44.5
    elif unit == "m":
        return value*1000
    elif unit =="s":
        return value*10
    elif unit == "f":
        return value*304.8
    elif unit == "mm":
        return value

kadets = {}

for i in range(0, int(input())):
    lastname, value, unit = map(str, input().split(" "))
    kadets[lastname] = convert_value_to_mm(value, unit)
    
srtd = sorted(kadets.items(), key=lambda x:x[1]) 
print(srtd[(len(srtd)//2)][0])