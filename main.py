def exersize1(num):
    # Напишите программу, которая выводит чётные числа из заданного списка
    # и останавливается, если встречает число 237.
    array = []
    for i in range(num-15, num+16):
        array.append(i)

    print("Заданный список: ", end="")
    for i in array:
        print(f"{i} ", end="")

    result = "Чётные числа: "
    for i in array:
        if i == num: break
        if i % 2 == 0:
            result += f"{i} "

    print(f"\n{result}")

    return 0
def exersize2(basenum, bordernum):
    # Ввести произвольное число в консоле
    # Ввести пограничное число в консоле
    # Если 1-ое число меньше пограничного, вывести сообщение об этом.
    # Если 1-ое число больше пограничного, вывести сообщение об этом.
    # Если 1-ое число больше пограничного более, чем в 3 раза, сообщить об этом

    if (basenum < bordernum):
        return "Произвольное число МЕНЬШЕ пограничного."
    elif (basenum > bordernum):
        if (basenum > 3 * bordernum):
            return "Произвольное число БОЛЬШЕ пограничного более, чем в 3 раза."
        return "Произвольное число БОЛЬШЕ пограничного."
    return "Произвольное число РАВНО пограничному."

if __name__ == '__main__':
    exersize1(237)
    basenum = int(input("Введите произвольное число: "))
    bordernum = int(input("Введите пограничное число: "))
    print(exersize2(basenum, bordernum))
