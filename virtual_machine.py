# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import deque
import sys
import os
import tokenize
from io import StringIO


class Stack(deque):
    push = deque.append

    def top(self):
        return self[-1]


def get_input(*args, **kw):
    """Read a string from standard input."""
    if sys.version[0] == 2:
        return raw_input(*args, **kw)
    else:
        return input(*args, **kw)


class Machine(object):

    def __init__(self, code):
        self.data_stack = Stack()
        self.return_addr_stack = Stack()
        self.instruction_pointer = 0
        self.code = code

    def pop(self):
        return self.data_stack.pop()

    def push(self, value):
        self.data_stack.push(value)

    def top(self):
        return self.data_stack.top()

    def run(self):
        while self.instruction_pointer < len(self.code):
            opcode = self.code[self.instruction_pointer]
            self.instruction_pointer += 1
            self.dispatch(opcode)

    def dispatch(self, op):
        dispatch_map = {
            "==":       self.eq,         "%":        self.mod,
            "+":        self.plus,       "-":        self.minus,
            "*":        self.mul,        "/":        self.div,
            "cast_int": self.cast_int,   "cast_str": self.cast_str,
            "drop":     self.drop,       "dup":      self.dup,
            "swap":     self.swap,       "over":     self.over,
            "print":    self.print,      "println":  self.println,
            "read":     self.read,       "exit":     self.exit,
            "if":       self.if_stmt,    "jmp":      self.jmp,
            "stack":    self.dump_stack, "clear":    self.clear,
        }

        if op in dispatch_map:
            dispatch_map[op]()
        elif isinstance(op, int):
            self.push(op)
        elif isinstance(op, str) and op[0] == op[-1] == '"':
            self.push(op[1:-1])
        else:
            raise RuntimeError("Unknown opcode: '%s'" % op)

    # Operations follow:

    def eq(self):
        self.push(self.pop() == self.pop())

    def mod(self):
        last = self.pop()
        self.push(self.pop() % last)

    def plus(self):
        self.push(self.pop() + self.pop())

    def minus(self):
        last = self.pop()
        self.push(self.pop() - last)

    def mul(self):
        self.push(self.pop() * self.pop())

    def div(self):
        last = self.pop()
        self.push(self.pop() / last)

    def cast_int(self):
        self.push(int(self.pop()))

    def cast_str(self):
        self.push(str(self.pop()))

    def drop(self):
        self.pop()

    def dup(self):
        self.push(self.top())

    def swap(self):
        b = self.pop()
        a = self.pop()
        self.push(b)
        self.push(a)

    def over(self):
        b = self.pop()
        a = self.pop()
        self.push(a)
        self.push(b)
        self.push(a)

    def print(self):
        sys.stdout.write(str(self.pop()))
        sys.stdout.flush()

    def println(self):
        sys.stdout.write("%s\n" % self.pop())
        sys.stdout.flush()

    def read(self):
        self.push(get_input())

    def exit(self):
        sys.exit(0)    

    def if_stmt(self):
        false_clause = self.pop()
        true_clause = self.pop()
        test = self.pop()
        self.push(true_clause if test else false_clause)

    def jmp(self):
        addr = self.pop()
        if isinstance(addr, int) and 0 <= addr < len(self.code):
            self.instruction_pointer = addr
        else:
            raise RuntimeError("JMP address must be a valid ineger.")

    def dump_stack(self):
        print("Data stack (top first):")
        for v in reversed(self.data_stack):
            print(" - type %s, value '%s'" % (type(v), v)) 

    def clear(self):
        os.system("clear")


def parse(text):
    if sys.version[0] == "2":
        stream = StringIO(unicode(text))
    else:
        stream = StringIO(text)

    tokens = tokenize.generate_tokens(stream.readline)

    for toknum, tokval, _, _, _ in tokens:
        if toknum == tokenize.NUMBER:
            yield int(tokval)
        elif toknum in [tokenize.OP, tokenize.STRING, tokenize.NAME]:
            yield tokval
        elif toknum == tokenize.ENDMARKER:
            break
        else:
            raise RuntimeError("Unknown token %s: '%s'" %
                               (tokenize.tok_name[toknum], tokval))

def constant_fold(code):
    while True:
        for i, (a, b, op) in enumerate(zip(code, code[1:], code[2:])):
            if isinstance(a, int) and isinstance(b, int) and (
                                      op in {"+", "-", "*", "/"}):
                m = Machine((a, b, op))
                m.run()
                code[i:i+3] = [m.top()]
                print("Constant-folded %s%s%s to %s" % (a, op, b, m.top()))
                break
            else:
                break
        return code


def repl():
    print('Hit CTRL+D or type "exit" to quit.')

    while True:
        try:
            source = get_input("> ")
            code = list(parse(source))
            code = constant_fold(code)
            Machine(code).run()
        except (RuntimeError, IndexError) as e:
            print("IndexError: %s" % e)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")


def test(code = [2, 3, "+", 5, "*", "println"]):
    print("Code before optimization: %s" % str(code))
    optimized = constant_fold(code)
    print("Code after optimization: %s" % str(optimized))

    print("Stack before running original program:")
    a = Machine(code)
    a.run()
    a.dump_stack()

    print("Stack after running optimized program:")
    b = Machine(optimized)
    b.run()
    b.dump_stack()

    result = a.data_stack == b.data_stack
    print("Result: %s" % ("OK" if result else "FAIL"))
    return result


# Examples follow:

'''
Machine([2, 3, "+", 4, "*", "println"]).run()
'''

'''
Machine([
    '"Enter a number: "', "print", "read", "cast_int",
    '"Enter another number: "', "print", "read", "cast_int",
    "over", "over",
    '"Their sum is: "', "print", "+", "println",
    '"Their product is: "', "print", "*", "println"
]).run()
'''

'''
Machine([
    '"Enter a number: "', "print", "read", "cast_int",
    '"The number "', "print", "dup", "print", '" is "', "print",
    2, "%", 0, "==", '"even"', '"odd"', "if", "println",
    0, "jmp"
]).run()  # loop forever!
'''


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            cmd = sys.argv[1]
            if cmd == "repl":
                repl()
            elif cmd == "test":
                test()
            else:
                print("Commands: repl, test")
        else:
            repl()
    except EOFError:
        print("")


