import numbers
import letters
import time
import os


def countdown(t: int = 30):
    print()
    for i in range(t):
        time.sleep(1)
        if not(i % 5):
            print(i)
    print("TIME'S UP\n")


def letters_round() -> (int, int):

    print("Letters Round")
    vows = int(input("How many vowels?\n"))
    cons = int(input("How many consonant?\n"))

    letts = letters.get_letters(cons, vows)
    print("Your Letters Are:\n")
    print(" ".join(letts))

    countdown()

    word1 = input("Player 1 type your word:\n")
    message, score1 = letters.word_score(word1, letts)
    print(f"{message} - Score: {score1} \n")

    word2 = input("Player 2 type your word:\n")
    message, score2 = letters.word_score(word2, letts)
    print(f"{message} - Score: {score2} \n")

    best = letters.best_words(letts)
    print("\nThe best words are:")
    print(" - ".join(best))
    time.sleep(2)

    return score1, score2


def numbers_round() -> (int, int):

    print("Numbers Round")
    sml = int(input("How many small?\n"))
    lrg = int(input("How many large?\n"))

    nums = numbers.get_numbers(sml, lrg)
    target = numbers.target()

    print(f"The numbers are: {'-'.join(map(str, nums))}")
    print(f"The target is: {target}\n")

    countdown()

    eqn1 = eval(input("Player 1 type your calculation or number:\n"))
    print(f"This is: {eqn1}")
    score1 = numbers.number_score(target, eqn1)
    print(f"You score: {score1}")

    eqn2 = eval(input("Player 2 type your calculation or number:\n"))
    print(f"This is: {eqn2}")
    score2 = numbers.number_score(target, eqn2)
    print(f"You score: {score2}")


    solution = numbers.solution(nums, target)
    print(f"\nSolution: {numbers.to_infix(solution)}\n")
    time.sleep(2)

    return score1, score2


def play_round(score1: int, score2: int, lett: bool = True) -> (int, int):
    print("\n-------\n")
    if lett:
        s1, s2 = letters_round()
    else:
        s1, s2 = numbers_round()

    score1 += s1
    score2 += s2
    print_scores(score1, score2)
    return score1, score2

def print_scores(sc1, sc2):
    os.system('clear')
    print(f"PLAYER 1 SCORE: {sc1} --- PLAYER 2 SCORE: {sc2}\n")


if __name__ == "__main__":

    print("COUNTDOWN\n")

    score1, score2 = 0, 0

    score1, score2 = play_round(score1, score2)
    score1, score2 = play_round(score1, score2)
    score1, score2 = play_round(score1, score2, lett=False)

    score1, score2 = play_round(score1, score2)
    score1, score2 = play_round(score1, score2)
    score1, score2 = play_round(score1, score2, lett=False)
