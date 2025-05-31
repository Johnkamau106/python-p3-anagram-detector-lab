class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        # Normalize the sorted characters of the original word
        sorted_word = sorted(self.word)
        matches = []

        for candidate in word_list:
            # Skip if it's the same as the original word
            if candidate.lower() == self.word:
                continue

            if sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)

        return matches
# your code goes here!
