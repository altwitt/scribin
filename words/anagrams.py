import itertools
import timeit
from collections import Counter, defaultdict

# Load the list of English words from the text file
with open("popular_25K.txt", "r") as file:
    english_words = set(word.strip() for word in file.readlines())


def find_anagrams(word):
    word = word.lower()
    anagrams = set()

    # Generate all possible permutations of the characters in the word
    for permutation in itertools.permutations(word):
        candidate = "".join(permutation)
        if candidate in english_words and candidate != word:
            anagrams.add(candidate)

    return anagrams


def main():
    input_strings = input(
        "Enter a string or a list of strings (comma-separated): "
    ).split(",")

    for input_str in input_strings:
        anagrams = find_anagrams(input_str)

        print(f"Anagrams for '{input_str}':")
        if anagrams:
            print(", ".join(anagrams))
        else:
            print("No anagrams found.")


def checking_anagram(keywords):
    agrms = defaultdict(list)
    for i in keywords:
        hist = tuple(Counter(i).items())
        agrms[hist].append(i)
    return list(agrms.values())


keywords = ("python", "yphotn")
print(checking_anagram(keywords))


if __name__ == "__main__":
    main()
timeit.timeit(main, number=1)
timeit.timeit(find_anagrams, number=1)
