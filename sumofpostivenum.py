def get_numbers_from_user():
    numbers = []
    n = int(input("How many numbers will you enter? "))
    for i in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)
    return numbers


def filter_negative_numbers(numbers):
    new_numbers = []
    for num in numbers:
        if num >= 0:
            new_numbers.append(num)
    return new_numbers


def sum_numbers(numbers):
    return sum(numbers)


def main():
    user_numbers = get_numbers_from_user()
    positive_numbers = filter_negative_numbers(user_numbers)
    total_sum = sum_numbers(positive_numbers)

    print(f"Sum of non-negative numbers: {total_sum}")


if __name__ == "__main__":
    main()



