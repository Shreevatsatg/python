import random
class guesstooheigh(Exception):
    pass    
class guesstooLow(Exception):
    pass
def guess_number(lower_limit, upper_limit):
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0
    while attempts < 5:
        try:
            guess = int(input(f'Guess the number between {lower_limit} and {upper_limit}: '))
            attempts += 1
            if guess < lower_limit or guess > upper_limit:
                raise ValueError("Guess is out of bounds.")
            if guess < secret_number:
                raise guesstooLow("Your guess is too low.")
            elif guess > secret_number:
                raise guesstooheigh("Your guess is too high.")
            else:
                print("Congratulations! You've guessed the number!")
                return
        except guesstooLow as e:
            print(e)
        except guesstooheigh as e:
            print(e)
        except ValueError as e:
            print(e)
    print(f'Sorry, you have used all attempts. The secret number was {secret_number}.')

def main():
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))
    if lower_limit >= upper_limit:
        print("Invalid range. Lower limit must be less than upper limit.")
        return
    guess_number(lower_limit, upper_limit)
main()