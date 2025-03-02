def calc(x, y):
    try:
        return int(x) / int(y)
    except ZeroDivisionError as err:
        print(err)
        return "На ноль делить нельзя"
    except ValueError:
        return "Ввел не число а хуйню"


print(calc(input("Number:"), input("Number:")))
print("Hello")
