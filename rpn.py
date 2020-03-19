from operator import add, sub, mul, truediv
from typing import List


Expression = List[int]

ops = {'+': add, '-': sub, '*': mul, '/': truediv}


class NotValidEqnError(BaseException):
    pass


def rpn(expr: Expression) -> int:
    stack = []
    for s in expr:
        if s in ops:
            try:
                stack.append(ops[s](stack.pop(), stack.pop()))
            except:
                raise NotValidEqnError
        else:
            stack.append(s)
    if len(stack) > 1: raise NotValidEqnError
    return int(stack[0])


def to_infix(expr: Expression) -> str:
    stack = []
    for s in expr:
        if s not in ops:
            stack = [s] + stack
        else:
            subexpr = f"({stack.pop(0)} {s} {stack.pop(0)})"
            stack= [subexpr] + stack

    return stack[0]
