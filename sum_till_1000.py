"""Write a script that asks the user to input numbers in a loop. The script will continuously calculate the sum of all the numbers typed.
When the sum reaches 1000 (or more), the loop will stop and the final sum will be printed."""
def main():


    total_sum = 0
    while total_sum < 1000:
        number = int(input("Enter a number: "))
        total_sum += number
    print(f"The sum of the numbers is:{total_sum} ")




if __name__ == "__main__":
    main()
