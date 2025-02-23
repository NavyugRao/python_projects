import random

def get_valid_input():
    """Loop until the user enters a valid number between 1 and 10."""
    while True:
        try:
            num = int(input("Enter your number (1-10): "))
            if 1 <= num <= 10:
                return num  # Return the valid input
            else:
                print("❌ Invalid input! Enter a number between 1 and 10.")
        except ValueError:
            print("❌ Invalid input! Please enter a NUMBER.")

def ball():
    runs_2 = set()  
    while True:
        z = get_valid_input()
        score1 = random.randint(1, 10)
        print(f"Computer chose: {score1}")
        
        if z != score1:
            runs_2.add(score1)
            print("Computer's score is:", sum(runs_2))
        else:
            print("Computer is OUT!\nFinal score:", sum(runs_2))
            break  
    return sum(runs_2)

def bat():
    runs = set()  
    while True:
        score1 = get_valid_input()
        z = random.randint(1, 10)
        print(f"Computer chose: {z}")

        if z != score1:
            runs.add(score1)
            print("Your score is:", sum(runs))
        else:
            print("You are OUT!\nFinal score:", sum(runs))
            break  
    return sum(runs)
