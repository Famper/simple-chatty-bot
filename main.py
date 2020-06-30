def greet(bot_name, birth_year):
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')
    print('Please, remind me your name.')
    name = str(input())
    print(f'What a great name you have, {name}!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem = [int(input()) for let in range(3)]
    age = (rem[0] * 70 + rem[1] * 21 + rem[2] * 15) % 105

    print(f"Your age is {age}; that's a good time to start programming!")


def count():
    print("Now I will prove to you that I can count to any number you want.")

    num = int(input())
    for let in range(num + 1):
        print(f"{let} !")


def test():
    text = (
        "Let's test your programming knowledge.",
        "Why do we use methods?",
        "1. To repeat a statement multiple times.",
        "2. To decompose a program into several small subroutines.",
        "3. To determine the execution time of a program.",
        "4. To interrupt the execution of a program."
    )

    for let in text:
        print(let)
    while True:
        ans = int(input())
        if ans == 2:
            break
        print("Please, try again.")
    print("Completed, have a nice day!")
    print("Congratulations, have a nice day!")


greet("Famper", 2020)
guess_age()
count()
test()
