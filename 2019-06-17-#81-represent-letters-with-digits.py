"""
Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""


def find_all_possible_letters(digit_to_letters, digits):
    res = []
    def backtrack(i, letters):
        if i == len(digits):
            res.append(letters)
            return
        for letter in digit_to_letters[digits[i]]:
            backtrack(i+1, letters + letter)
    backtrack(0, '')
    return res


if __name__ == "__main__":
    digit_to_letters = {"2": ["a", "b", "c"], "3": ["d", "e", "f"]}
    digits = "23"
    print(find_all_possible_letters(digit_to_letters, digits))
