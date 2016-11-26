#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
    class for testing Collatz.py
    """

    # ----
    # read
    # ----

    def test_read_1(self):
        """ test reading capability """
        string = "1 10\n"
        start, end = collatz_read(string)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        """ test reading capability """
        string = "4 16\n"
        start, end = collatz_read(string)
        self.assertEqual(start, 4)
        self.assertEqual(end, 16)

    def test_read_3(self):
        """ test reading capability """
        string = "87 936\n"
        start, end = collatz_read(string)
        self.assertEqual(start, 87)
        self.assertEqual(end, 936)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """ test evaluating capability """
        max_cycle = collatz_eval(1, 10)
        self.assertEqual(max_cycle, 20)

    def test_eval_2(self):
        """ test evaluating capability """
        max_cycle = collatz_eval(100, 200)
        self.assertEqual(max_cycle, 125)

    def test_eval_3(self):
        """ test evaluating capability """
        max_cycle = collatz_eval(201, 210)
        self.assertEqual(max_cycle, 89)

    def test_eval_4(self):
        """ test evaluating capability """
        max_cycle = collatz_eval(900, 1000)
        self.assertEqual(max_cycle, 174)

    def test_eval_5(self):
        """ test evaluating capability """
        max_cycle = collatz_eval(1, 1)
        self.assertEqual(max_cycle, 1)

    def test_eval_6(self):
        """ test evaluating capability """
        max_cycle = collatz_eval(999999, 1)
        self.assertEqual(max_cycle, 525)

    def test_eval_7(self):
        """ test evaluating capability """
        max_cycle = collatz_eval(10, 10)
        self.assertEqual(max_cycle, 7)

    def test_eval_8(self):
        """ test evaluating capability """
        max_cycle = collatz_eval(9, 6)
        self.assertEqual(max_cycle, 20)

    def test_eval_9(self):
        """ test evaluating capability """
        max_cycle = collatz_eval(1, 1000)
        self.assertEqual(max_cycle, 179)

    def test_eval_10(self):
        """ test evaluating capability """
        max_cycle = collatz_eval(6, 6)
        self.assertEqual(max_cycle, 9)

    def test_eval_11(self):
        """ test evaluating capability """
        max_cycle = collatz_eval(27, 27)
        self.assertEqual(max_cycle, 112)

    # -----
    # print
    # -----

    def test_print_1(self):
        """ test printing capability """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """ test printing capability """
        writer = StringIO()
        collatz_print(writer, 6, 6, 9)
        self.assertEqual(writer.getvalue(), "6 6 9\n")

    def test_print_3(self):
        """ test printing capability """
        writer = StringIO()
        collatz_print(writer, 108, 108, 114)
        self.assertEqual(writer.getvalue(), "108 108 114\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """ test solving capability """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """ test solving capability """
        reader = StringIO("1 1\n2 2\n3 3\n5 5\n10 10\n9 9\n7 7\n6 6\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 1 1\n2 2 2\n3 3 8\n5 5 6\n10 10 7\n9 9 20\n7 7 17\n6 6 9\n")

    def test_solve_3(self):
        """ test solving capability """
        reader = StringIO("100 171\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "100 171 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()