import random as rd
from freq import frequency as ALPHABET
from typing import List, Set, Generator
from collections import Counter, defaultdict
from itertools import combinations, product


Letters = str
Numbers = str
Word = str
Words = List[Word]


VOWELS = {k: v for k, v in ALPHABET.items() if k in "aeiou"}
CONSONANTS = {k: v for k, v in ALPHABET.items() if k not in VOWELS}

join = "".join
def key(x): return join(sorted(x))
def shuffled(x): return sorted(x, key=lambda _: rd.random())


with open("data/enable1.txt") as f:
    WORDS = (w for w in f.read().split() if len(w) < 10)


WORD_MAP = defaultdict(list)
for w in WORDS:
    WORD_MAP[key(w)] += [w]


def get_letters(n_cons: int, n_vows: int) -> Letters:
    v = rd.choices(list(VOWELS), weights=VOWELS.values(), k=n_vows)
    c = rd.choices(list(CONSONANTS), weights=CONSONANTS.values(), k=n_cons)
    return join(sorted(v + c, key=lambda _: rd.random()))


def lettersets(letters: Letters) -> Set[Word]:
    return {key(l) for i in range(4, 9) for l in combinations(letters, i)}


def letter_match(word: Word, letters: Letters) -> bool:
    c = Counter(letters)
    c.subtract(word)
    return all(v >= 0 for v in c.values())


def word_score(word: Word, letters: Letters) -> int:
    if word not in WORDS:
        return "Not a word", 0

    if not letter_match(word, letters):
        return "You've used a letter that's not there", 0

    m = "Good word!"
    return (m, 18) if len(word) is 9 else (m, len(word))


def best_words(letters: Letters, n: int = 5) -> Words:
    poss = [WORD_MAP[s] for s in lettersets(letters) if s in WORD_MAP]
    return sorted(sum(poss, []), key=len, reverse=True)[:n]


def conundrums() -> Generator[Word, None, None]:

    uniq9s = {k: v for k, v in WORD_MAP.items() if len(v) is 1 and len(k) is 9}
    fours = shuffled(w for w in WORDS if len(w) is 4)
    fives = shuffled(w for w in WORDS if len(w) is 5)

    for fr, fv in product(fours, fives):
        k = join(sorted(fr + fv))
        if k in uniq9s:
            yield fr, fv, uniq9s[k][0]
