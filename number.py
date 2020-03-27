from itertools import (combinations, permutations,
        combinations_with_replacement, product)
from rpn import to_infix, rpn as calc
from toolz import mapcat
from typing import Tuple, Generator
import random as rd


Numbers = Tuple[int]
Equations = Generator[Numbers, None, None]


SMALL = list(range(1, 11)) * 2
LARGE = [25, 50, 75, 100] * 2

join = "".join


def number_score(target: int, guess: int) -> int:
    if abs(target - guess) < 1:
        return 10
    if abs(target - guess) < 6:
        return 7
    if abs(target - guess) < 11:
        return 5
    return 0


def get_numbers(n_sml: int, n_lrg: int) -> Numbers:
    return rd.choices(SMALL, k=n_sml) + rd.choices(LARGE, k=n_lrg)


def target() -> int:
    return int(rd.uniform(100, 1000))


def eqn_nums(nums: Numbers) -> Equations:
    # all combs/perms of ops
    ops = combinations_with_replacement("+-/*", len(nums) - 1)
    op_perms = mapcat(permutations, ops)
    # all number permutations, compute these now (not a gen)
    # and take the set, this will save on redundant eqns
    num_perms = set(permutations(nums))

    eqns = product(num_perms, op_perms)
    return (list(p) + list(o) for p, o in eqns)


def all_eqn(nums: Numbers) -> Equations:
    for i in range(4, len(nums) + 1):
        for n in combinations(nums, i):
            yield from eqn_nums(n)


def is_solution(nums: Numbers, t: target) -> bool:
    try:
        return calc(nums) == t
    except NotValidEqnError:
        return False


def solution(nums: Numbers, t: target) -> Numbers:
    return next(filter(lambda x: is_solution(x, t), all_eqn(nums)), [''])
