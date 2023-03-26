
print(" 1. addition \n 2. subtraction \n 3. multiplication \n 4. division \n 5. exit ")


def add(num_1, num_2):
    result = num_1 + num_2
    print(f' result = {result}')


def sub(num_1, num_2):
    result = num_1 - num_2
    print(f' result = {result}')


def mul(num_1, num_2):
    result = num_1 * num_2
    print(f' result = {result}')


def div(num_1, num_2):
    result = num_1 / num_2
    print(f' result = {result}')


while True:
    choice = (int(input(
        " What arithmetic operation do you want to perform ? \n specify by selecting a number from 1 to 5  : ")))

    if (choice >= 1 and choice <= 4):

        var_1 = (int(input(" First number : ")))
        var_2 = (int(input(' Second number ')))

        if (choice == 1):
            add(var_1, var_2)

        elif (choice == 2):
            sub(var_1, var_2)

        elif (choice == 3):
            mul(var_1, var_2)

        elif (choice == 4):
            div(var_1, var_2)

    elif (choice == 5):
        print(' Please wait!!!! \n Terminating program.....')
        break

    else:
        print("Sorry, what you specify isn't in the options given above \n Try again....")
