import random
import inflect

def main():
    p = inflect.engine()

    one = 1
    seven_hundred_billion = 700_000_000_000

    im_thinking_of_a_number_between = random.randint(one, seven_hundred_billion)
    print('I\'m thinking of a number between one and seven hundred billion. Try to guess it.')

    try_to_guess_it = True
    while try_to_guess_it:
        guess = random.randint(one, seven_hundred_billion)
        print(p.number_to_words(guess))
        try_to_guess_it = (guess != im_thinking_of_a_number_between)
        if try_to_guess_it:
            print('Nope. Guess again.')
            
if __name__ == '__main__':
    main()
