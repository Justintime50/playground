import json
import string
from collections import Counter, defaultdict

# Place letters here that were incorrect and cannot be used again
DEAD_LETTERS = []

# Place letters here that were correct, but not in the right position (yellow background)
# and say what index they didn't work in, eg:
# {
#     "e": [0, 1],
#     "i": [2, 4],
#     "n": [0, 3],
#     "c": [2],
# }
CORRECT_LETTERS_WRONG_POSITIONS = {}

# Place your word guess here (starting word is `serai`)
VERIFIED_LETTERS = ["", "", "", "", ""]
STARTING_LETTER = ""  # TODO: This is janky but is a poor mans approach for now


"""Do not edit code below this line!"""
ALPHABET = string.ascii_lowercase


# TODO: Assign weights and distribution to the probabilities to choose the next best guess


def main():
    """Wordle has two sets of lists (distinction unknown), all words in the lists are unique and
    are exactly 5 letters long.

    A good initial guess would be `serai` as it contains the most used letters and starts with
    the most started with letter and does not contain duplicates.
    """
    # TODO: Longterm we should grab the lists from the site in the chance they get updated overtime
    short_list = _read_file("solver/short_list.json")
    long_list = _read_file("solver/long_list.json")
    combined_lists = short_list + long_list

    total_numbers = len(short_list + long_list)
    print("Total number of Wordles: ", total_numbers)

    # get_most_common(combined_lists)

    get_best_guess(combined_lists)


def get_most_common(possible_words):
    """Gets the most common starting letters and letters overall.

    This is ultimately an exploratory tool used during development to inspect what's happening
    under the hood of the lists chosen by Wordle. This may not be super helpful to someone using
    this tool to simply find the best guess.
    """
    letter_start_count = defaultdict(int)
    letter_counts = defaultdict(int)

    # TODO: There are better ways than a double (triple) nested for loop (could we use zip instead?)
    for word in possible_words:
        for letter in ALPHABET:
            if word.startswith(letter):
                letter_start_count[letter] += 1
            for letter in word:
                if letter in ALPHABET:
                    letter_counts[letter] += 1

    most_common_start = Counter(letter_start_count).most_common()
    most_common_letters = Counter(letter_counts).most_common()
    print("Most common starting letter", most_common_start)
    print("Most common letters", most_common_letters)

    get_best_word(most_common_letters, possible_words)


def get_best_word(most_common_letters, possible_words):
    # TODO: We'll want to also weigh in probability of if the starting letter is verified yet or not
    # and use the most probable one if not yet
    letter_probabilities = sorted(
        list(set(most_common_letters) - set(DEAD_LETTERS)),
        key=lambda x: x[1],
        reverse=True,
    )
    print("Letter probabilities: ", letter_probabilities)

    for word in possible_words:
        word_failed = False
        letters_that_match_criteria = 0
        for letter in [possible_letter[0] for possible_letter in letter_probabilities]:
            for (
                correct_letter,
                bad_positions,
            ) in CORRECT_LETTERS_WRONG_POSITIONS.items():
                for bad_position in bad_positions:
                    if correct_letter == word[bad_position]:
                        word_failed = True
            if letter in word:
                letters_that_match_criteria += 1
        if letters_that_match_criteria == 5 and not word_failed:
            if (
                STARTING_LETTER
                and word.startswith(STARTING_LETTER)
                or not STARTING_LETTER
            ):
                print(word)


def get_best_guess(combined_lists):
    """Get the best guess based on probability from what's been eliminated,
    what was guess correctly, and what letters remain.
    """
    # TODO: Could we use zip here instead?
    possible_words = []
    for word in combined_lists:
        word_failed = False
        for dead_letter in DEAD_LETTERS:
            if dead_letter in word:
                word_failed = True
                break
        for correct_letter in CORRECT_LETTERS_WRONG_POSITIONS:
            if correct_letter not in word:
                word_failed = True
                break

        if word_failed is True:
            # do nothing as the word is not valid
            pass
        else:
            possible_words.append(word)

    print("Possible words: ", len(possible_words))
    # print(possible_words)

    get_most_common(possible_words)


def _read_file(filename):
    with open(filename, "r") as data:
        word_list = json.load(data)

    return word_list


if __name__ == "__main__":
    main()
