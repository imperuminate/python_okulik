num = 34

while True:
    user_num = int(input("User num:"))
    if num == user_num:
        break
    elif num > user_num:
        print("Enter highter number")
    else:
        print("Enter lower number")

