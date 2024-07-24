def calculate(text_input):
    if "+" in text_input:
        number1, number2 = text_input.split("+")
        addition = int(number1) + int(number2)
        return addition
    elif "*" in text_input:
        number1, number2 = text_input.split("*")
        multiplication = int(number1) * int(number2)
        return multiplication
    elif "/" in text_input:
        number1, number2 = text_input.split("/")
        division = int(number1) / int(number2)
        return division
    elif "-" in text_input:
        number1, number2 = text_input.split("-")
        subtraction = int(number1) - int(number2)
        return subtraction
    elif "~" in text_input:
        number1, number2 = text_input.split("~")
        integer_division = int(number1) / int(number2)
        remainder = int(number1) % int(number2)
        return f"{int(integer_division)}\nThe remainder is {remainder}"


print("Welcome to the Python calculator!")
no_of_calculation = int(input("How many calculations do you want to do? "))
for i in range(no_of_calculation):
    user_input = input("What do you want to calculate? ")
    result = calculate(user_input)
    print(f"The answer is {result}")