from operator import add, sub, mul, truediv
from typing import List


Expression = List[int]

ops = {'+': add, '-': sub, '*': mul, '/': truediv}


class NotValidEqnError(BaseException):
    pass


def is_natural(x):
    return (x > 0) and (x % 1 == 0)


def rpn(expr: Expression) -> int:
    # Interestingly this is ~10x faster than writing the
    # eqn in infix and eval-ing it
    stack = []
    for s in expr:
        if s in ops:
            try:
                n = ops[s](stack.pop(), stack.pop())
                # no non-naturals
                if not is_natural(n): return None
                stack.append(n)
            except:
                raise NotValidEqnError
        else:
            stack.append(s)
    if len(stack) > 1: raise NotValidEqnError
    return stack[0]


def to_infix(expr: Expression) -> str:
    stack = []
    for s in expr:
        if s not in ops:
            stack = [s] + stack
        else:
            subexpr = f"({stack.pop(0)} {s} {stack.pop(0)})"
            stack= [subexpr] + stack

    return stack[0]
