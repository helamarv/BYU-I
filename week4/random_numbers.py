import random
import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")

    append_random_numbers(numbers)
    print(f"numbers {numbers}")

    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")

    # Create a list to store random words.
    words = []

    append_random_words(words)
    print(f"words {words}")

    append_random_words(words, 5)
    print(f"words {words}")


def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)


def append_random_words(words_list, quantity=1):

    # A list of words to randomly choose from.
    candidates = [
        "arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"
    ]

    # Randomly choose quantity words and append them onto words_list.
    for _ in range(quantity):
        word = random.choice(candidates)
        words_list.append(word)

if __name__ == "__main__":
    main()







