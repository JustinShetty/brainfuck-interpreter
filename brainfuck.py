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
        self.loop_pos_ = []

    def run(self, filename):
        with open(filename, 'r') as f:
            chars = [
                ch for line in f.readlines()
                for ch in line.rstrip().replace(' ', '')
            ]
            ops = [ch for ch in chars if ch in self.VALID_OPS]
            self.evaluate(ops)

    def evaluate(self, ops):
        op_idx = 0
        while op_idx < len(ops):
            op = ops[op_idx]
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
            elif op == '[':
                self.loop_pos_.append(op_idx)
            elif op == ']':
                if self.memory_[self.mem_idx_] == 0:
                    self.loop_pos_.pop()
                else:
                    op_idx = self.loop_pos_[-1]
            op_idx += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Brainfuck Interpreter")
    parser.add_argument('input_filename',
                        type=str,
                        help='ASCII-encoded source file')
    args = parser.parse_args()
    bf = Brainfuck()
    bf.run(args.input_filename)
