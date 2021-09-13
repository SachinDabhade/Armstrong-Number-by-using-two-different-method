
# ********************** Find angstrom number with two different methods ****************************

# This is the practice problem on how to find amstorong numbers in the python programme
def Armstrong_1(number):
    output = 0
    for num in str(number):
        Num = int(num) ** len(str(number))
        output = Num + output
    if number == output:
        print("This is the Armstrong number...!")
    else:
        print("This is not the Armstrong number...!")

# This function will give me the anstrong number output
def Armstrong_2(number):
    copyNum = number
    order = len(str(number))
    output = 0
    while number > 0:
        digit = number % 10
        output += digit ** order
        number = number // 10
    if copyNum == output:
        print("This is the Armstrong number...!")
    else:
        print("This is not the Armstrong number...!")


if __name__ == '__main__':
    while True:
        try:
            number = int(input("Enter the number: "))
        except ValueError as E:
            print("Only Integers are allowed...!")
        else:
            Armstrong_1(number)
            Armstrong_2(number)
        continue
