my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
polo_ch = []
index = 0
while index < len(my_list):
    znach = my_list[index]
    if znach > 0:
        polo_ch.append(znach)
    if znach < 0:
        break
    index += 1
print(polo_ch)

