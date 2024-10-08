import random
import string
import requests

class Game:
    def __init__(self) -> None:
        """Initialize a random grid of size 9"""
        self.grid = self.generate_random_grid()

    def generate_random_grid(self) -> list:
        """Generate a random 3x3 grid of uppercase letters"""
        return [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy()
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']
