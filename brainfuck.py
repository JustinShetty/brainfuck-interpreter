#!/usr/bin/env python3
#
# Author: Justin Shetty
# Date:   30 January 2020
#
import sys
import argparse


class Brainfuck:
    VALID_OPS = '><+-.,[]'

    def __init__(self):
        self.memory_ = [0]
        self.mem_len_ = 1
        self.mem_idx_ = 0

    def run(self, filename):
        opstring = self.parse_ops(filename)
        self.evaluate(opstring)

    def parse_ops(self, filename):
        with open(filename, 'r') as f:
            return ''.join([ch for ch in f.read() if ch in self.VALID_OPS])

    def bracket_pairing(self, opstring):
        brackets = {}
        stack = []
        for i, op in enumerate(opstring):
            if op == '[':
                stack.append(i)
            elif op == ']':
                opener = stack.pop()
                brackets[opener] = i
                brackets[i] = opener
        return brackets

    def evaluate(self, opstring):
        brackets = self.bracket_pairing(opstring)
        op_idx = 0
        while op_idx < len(opstring):
            op = opstring[op_idx]
            if op == '>':
                self.mem_idx_ += 1
                if self.mem_idx_ == self.mem_len_:
                    self.mem_len_ += 1
                    self.memory_.append(0)
            elif op == '<':
                self.mem_idx_ -= 1
                if self.mem_idx_ < 0:
                    raise IndexError('Index -1 outside bounds')
            elif op == '+':
                self.memory_[self.mem_idx_] += 1
            elif op == '-':
                self.memory_[self.mem_idx_] -= 1
            elif op == '.':
                sys.stdout.write(chr(self.memory_[self.mem_idx_]))
            elif op == ',':
                self.memory_[self.mem_idx_] = sys.stdin.read(1)
            elif op == '[' and self.memory_[self.mem_idx_] == 0:
                op_idx = brackets[op_idx]
            elif op == ']' and self.memory_[self.mem_idx_] != 0:
                op_idx = brackets[op_idx]
            op_idx += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Brainfuck Interpreter")
    parser.add_argument('input_filename',
                        type=str,
                        help='ASCII-encoded source file')
    args = parser.parse_args()
    bf = Brainfuck()
    bf.run(args.input_filename)
