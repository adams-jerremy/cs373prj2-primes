#!/usr/bin/env python



# To run the tests
#     TestCollatz.py

# To document the tests
#     pydoc -w TestCollatz

import main
import unittest

# ----------
# TestReader
# ----------

class TestReader (object) :
    def __init__ (self, s) :
        self.s = s

    def read (self) :
        return self.s

# ----------
# TestWriter
# ----------

class TestWriter (object) :
    def str (self) :
        return self.s

    def write (self, *a) :
        self.s = str(a[0])
        for w in a[1:] :
            self.s += ' '
            self.s += str(w)
        self.s += '\n'

# -----------
# TestCollatz
# -----------

class TestPrimes (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        reader = TestReader('403\n')
        main.my_read(reader)
        self.assert_(main.i ==  403)

    # ----
    # eval
    # ----

    def test_eval1 (self) :
        main.i =  10
        main.p1 = 0
        main.p2 = 0
        main.my_eval(main.i-4)
        self.assert_(main.p1 == 3 )
        self.assert_(main.p2 == 3 )
    def test_eval2 (self) :
        main.i =  24
        main.p1 = 0
        main.p2 = 0
        main.my_eval(main.i-4)
        self.assert_(main.p1 == 3 )
        self.assert_(main.p2 == 17 )
    def test_eval3 (self) :
        main.i =  36
        main.p1 = 0
        main.p2 = 0
        main.my_eval(main.i-4)
        self.assert_(main.p1 == 3 )
        self.assert_(main.p2 == 29 )
    def test_eval4 (self) :
        main.i =  10000000
        main.p1 = 0
        main.p2 = 0
        main.my_eval(main.i-4)
        self.assert_(main.p1 == 5 )
        self.assert_(main.p2 == 9999991 )            
    # -----
    # print
    # -----

    def test_print (self) :
        main.i =  2
        main.p1 = 10
        main.p2 = 20
        writer = TestWriter()
        main.my_print(writer)
        self.assert_(writer.str() == '2 2 10 20\n')

if __name__ == "__main__" :
    unittest.main()
