# Binary to Decimal and Back Converter
# Wallis


def decimaltobinary(number):
    binary = []
    x = 0
    while number > 0:
        binary.append(number % 2)
        number = int(number / 2)
        x += 1
    print("".join(map(str, binary[::-1])))


def binarytodecimal(number):
    power = 0
    binary_num = list(map(int, str(number)))
    binary_num = binary_num[::-1]
    decimal_num = []
    while len(binary_num) > power:
        if binary_num[power] == 1:
            x = 2 ** power
            decimal_num.append(x)
            power += 1
        else:
            power += 1
            continue
    print(sum(decimal_num))


while True:
    try:
        choice = int(input('Do you want to convert binary to decimal(1) or decimal to binary(2): '))
    except:
        print('You need to type 1 or 2')
    if choice == 1:
        binary = int(input('Enter a binary number: '))
        binarytodecimal(binary)
    else:
        decimal = int(input('Enter a decimal number: '))
        decimaltobinary(decimal)
