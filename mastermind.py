import random


def get_guess():
    while True:
        # Checks length
        guess = input("Guess: ")
        if len(guess) != 4:
            print("Your guess must consist of 4 numbers.")
            continue
        temp = True
        # Checks if the correct number is used
        for letter in guess:
            if int(letter) < 1 or int(letter) > 7:
                print("You can only use number 1-7 as guesses.")
                temp = False
                break

        if not temp:
            continue

        return [int(num) for num in guess]


def check_values(code, user):
    result = []

    for item in user:
        if item in code and code.index(item) == user.index(item):
            result.append("Red")
        elif item in code:
            result.append("White")
        else:
            result.append("Black")
    random.shuffle(result)

    # If check_win is true, it returns an empty string. This is because
    # nothing will be printed, and the empty string is a falsy value
    if check_win(result):
        return ''
    return result


def check_win(response_list):
    if response_list.count("Red") == 4:
        print("Congratulations! You Win!")
        return True


# This creates
def create_comp_list():
    random_list = []
    while len(random_list) != 4:
        num = random.randint(1, 7)
        random_list.append(num)
    random.shuffle(random_list)
    return random_list


# Overall game loop
def play_game():
    code = create_comp_list()
    for i in range(12):
        print("Guesses Remaining: " + str(12 - i))
        user = get_guess()
        result = check_values(code, user)
        print(result)

        if not result:
            break


# Prints directions so the user knows how the game works!

print("Welcome to Mastermind! Your goal is to correctly guess the secret code!")
print("When you enter a guess, you'll receive a list of colors.")
print("Red means that a number is in the correct spot, White means that the number is correct \
but the position isn't, and black means that the number is incorrect.")
print("Please note that the list of colors does not correlate to the position of each number in the guess.")
play_game()