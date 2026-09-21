
import random
from importlib.resources import files
from rich.console import Console
console = Console()
def main():
    words = load_words(files("atk.wordle").joinpath("words.txt"))
    valid_words = load_words(files("atk.wordle").joinpath("allowed_words.txt"))
    streak = 0
    best = 0
    choice = 'y'
    while choice == 'y':
        answer = random.choice(words)
        
        count = 0
        while count < 6:
            while True:
                guess = input("Enter your guess: ")
                if len(guess) == 5 and guess in valid_words:
                    break
                elif len(guess) != 5:
                    print("Guess must be 5 letters.")
                else:
                    print("Not a valid word.")
                
            if guess == answer:
                print_guess(guess, check_guess(guess, answer))
                streak +=1
                if streak > best:
                    best = streak
                print(f"Streak: {streak}")
                print(f'Best: {best}')
                break
            else:
                print(f"Wrong! {count+1} out of 6 attempts!")
                print_guess(guess, check_guess(guess, answer))
                count+= 1
                if count == 6:
                    print("Out of guesses!")
                    print(f'You had a streak of {streak} and your best streak was {best}!')
                    streak = 0
        choice = input("Press 'y' to continue: ")

def check_guess(guess, answer):
    result = [None] * 5
    answer_list = list(answer)
    for i in range(5):
        if guess[i] == answer[i]:
            result[i] = "green"
            answer_list.remove(guess[i])
        elif guess[i] in answer_list:
            result[i] = "yellow"
            answer_list.remove(guess[i])
        else:
            result[i] = "gray"
    return result
def print_guess(guess: str, result: list[str]):
    for letter, status in zip(guess, result):
        if status == "green":
            console.print(letter, style="bold white on green", end="")
        elif status == "yellow":
            console.print(letter, style="bold white on yellow", end="")
        else:
            console.print(letter, style="bold white on grey37", end="")
    console.print()
def load_words(file): 
    words = []
    with open(file) as f:
            for line in f:
                words.append(line.strip())
    return words

if __name__ == "__main__":
    main()