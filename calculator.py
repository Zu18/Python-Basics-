
MAX_ATTEMPTS = 3


class OutOfAttempts(Exception):
    pass



def all_logs_input(input):
    file = open("calculator_log.txt","a")
    file.write("\n" + str(input))
    file.close()


def logs_file():
    file = open("calculator_log.txt","a")
    file.write("\n" + str(number1))
    file.write(" " + operator + " ")
    file.write(str(number2))
    file.write(" = " + str(result))
    file.close()


def read_number(prompt):
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        try:
            text = input(prompt).strip()
            all_logs_input(text)
            return float(text)
        except ValueError:
            attempts += 1
            print("Oops!  That was no valid number.")
    raise OutOfAttempts


def read_operator():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        text = input("Enter operator(+, -, *, /):").strip()
        all_logs_input(text)
        if text in ('+', '-', '*', '/'):
            return text
        else:
            attempts += 1
            print("Oops!  That was no valid operator.")
    raise OutOfAttempts




try:
    number1 = read_number("Enter number1:")
    operator = read_operator()
    number2 = read_number("Enter number2:")
except OutOfAttempts:
    print("You run out of attempts")
    exit()


if '+' == operator:
    result = number1 + number2
elif '-' == operator:
    result = number1 - number2
elif '*' == operator:
    result = number1 * number2
elif '/' == operator:
    result = number1 / number2
else:
    print("Unsupported operator " + operator) # for future operators
    exit()
print(result)
logs_file()
