import random
def guessing_game():
        print("Welcome to The number game ")

        a = int(input("Enter the lower bound (X) of the range: "))
        b = int(input("Enter the upper bound (Y) of the range: "))
        
        # additional things 
        if a > b:
            print("The lower bound must be less than or equal to the upper bound. Please try again.")
            return

        secret_number = random.randint(a, b)
        attempts = 0

        print(f"\nNow try to guess the number in minimum num of attempts!")

        while True:
           
                guess_num = int(input("Enter your guess: "))
                attempts += 1

                if guess_num < secret_number:
                    print("Too low! Try again.")
                elif guess_num > secret_number:
                    print("Too high! Try again.")
                else:
                      print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                      print("\n Thank u for playing !")
                break
                
guessing_game()



