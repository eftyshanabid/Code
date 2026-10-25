def main():

    number = int(input("Enter a number : "))

    if number == 0 :
        print("Zero")
    else :
        if number > 0:
            print(f"The {number} is a positive number")
        else :
            print(f"The {number} is a negative number")
        if number % 2 == 0:
            print(f"Ther {number} is even number")
        else :
            print(f"The {number} is odd number")

main()