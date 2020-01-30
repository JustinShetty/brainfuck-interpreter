#!/usr/bin/env python3
import sys
import argparse


class Brainfuck:
    VALID_OPS = '><+-.,[]'

    def __init__(self):
        self.memory_ = [0]
        self.memory_len_ = 1
        self.data_ptr_ = 0

    def run(self, filename):
        with open(filename, 'r') as f:
            chars = [ch for line in f.readlines() for ch in line.rstrip().replace(' ', '')]
            ops = [ch for ch in chars if ch in self.VALID_OPS]
            self.evaluate(ops)

    def evaluate(self, ops):
        for i in range(len(ops)):
            op = ops[i]
            if op == '>':
                self.data_ptr_ += 1
                if self.data_ptr_ == self.memory_len_:
                    self.memory_len_ += 1
                    self.memory_.append(0)
            elif op == '<':
                self.data_ptr_ -= 1
                if self.data_ptr_ < 0:
                    raise IndexError('Index -1 outside memory bounds')
            elif op == '+':
                self.memory_[self.data_ptr_] += 1
            elif op == '-':
                self.memory_[self.data_ptr_] -= 1
            elif op == '.':
                sys.stdout.write(chr(self.memory_[self.data_ptr_]))
            elif op == ',':
                self.memory_[self.data_ptr_] = sys.stdin.read(1)
            elif op == '[':
                pass
            elif op == ']':
                pass


def main(args):
    bf = Brainfuck()
    bf.run(args.input_filename)
    # print(bf.memory_)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Brainfuck Interpreter")
    parser.add_argument('input_filename', type=str, help='ASCII-encoded source file')
    args = parser.parse_args()
    main(args)
