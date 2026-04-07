import random
List_of_words = ["python", "programming", "computer", "algorithm", "variable",
    "function", "database", "network", "interface", "keyboard",
    "science", "library", "software", "hardware", "internet",
    "balloon", "coffee", "cheese", "rabbit", "summer",
    "success", "galaxy", "whisper", "puzzling", "journey",
    "mountain", "crystal", "diamond", "backpack", "adventure",
    "ice cream", "x-ray", "well-being", "high-tech" ]

def computer_chosen_word(words):
    chosen_word = random.choice(words)
    return chosen_word

computer_chosen_word(List_of_words)