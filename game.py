import number
import letters
import time
import subprocess
import os


def countdown():
    cmd = ["mpg123", "data/Countdown.mp3"]
    with open(os.devnull, 'wb') as devnull:
        subprocess.check_call(cmd, stdout=devnull, stderr=subprocess.STDOUT)
    print("TIME'S UP\n")


def letters_round(n_players: int):

    print("Letters Round")
    vows = int(input("How many vowels?\n"))
    cons = 9 - vows
    print(f"And you get {cons} consonants")

    letts = letters.get_letters(cons, vows)
    print("Your Letters Are:\n")
    print(" ".join(letts.upper()))

    countdown()

    scores = []
    for i in range(n_players):
        i += 1
        word1 = input(f"Player {i} type your word:\n")
        message, score = letters.word_score(word1, letts)
        print(f"{message} - Score: {score} \n")
        scores.append(score)

    best = letters.best_words(letts)
    print("\nThe best words are:")
    print(" - ".join(best))
    time.sleep(2)

    return set_scores(scores)


def numbers_round(n_players: int) -> list:

    print("Numbers Round")
    sml = int(input("How many small?\n"))
    lrg = 6 - sml

    nums = number.get_numbers(sml, lrg)
    target = number.target()

    print(f"The numbers are: {'-'.join(map(str, nums))}")
    print(f"The target is: {target}\n")

    countdown()

    scores = []
    for i in range(n_players):
        i += 1
        eqn = eval(input(f"Player {i} type your calculation or number:\n"))
        print(f"This is: {eqn}")
        score = number.number_score(target, eqn)
        print(f"You score: {score}")
        scores.append(score)


    solution = number.solution(nums, target)
    print(f"\nSolution: {number.to_infix(solution)}\n")
    time.sleep(2)

    return set_scores(scores)


def set_scores(scores:list) -> list:
    return [s if s == max(scores) else 0 for s in scores]


def add_scores(a: list, b: list) -> list:
    return [ai + bi for ai, bi in zip(a, b)]


def play_round(scores: list, round_type = letters_round) -> (int, int):
    print("\n-------\n")
    s = round_type(len(scores))

    scores = add_scores(scores, s)

    print_scores(scores)
    return scores


def print_scores(scores: list):
    os.system('clear')
    out = [f"PLAYER {i+1} SCORE: {s}" for i, s in enumerate(scores)]
    print(" ---- ".join(out))
    print("\n")


def play_section(scores: list) -> list:
    scores = play_round(scores)
    scores = play_round(scores)
    scores = play_round(scores, numbers_round)
    return scores


if __name__ == "__main__":

    print("COUNTDOWN\n")

    score = [0, 0]

    for i in range(3):
        score = play_section(score)
