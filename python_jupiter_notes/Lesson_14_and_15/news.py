num = 34


while True:
    user_num = int(input("User num:"))
    if num == user_num:
        break
    elif num > user_num:
        print("Enter highter number")
    else:
        print("Enter lower number")


while (user_num := int(input("User num:"))) != num:
    if num > user_num:
        print("Enter highter number")
    else:
        print("Enter lower number")


while True:
    user_input = input("Say something:")
    match user_input:
        case "Hi":
            print("Hello")
        case "":
            print("You nead to say something")
        case "Buy":
            break
        case _:
            print("??")
