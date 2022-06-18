# TODO: add suitable tests

import unittest
from re import sub
from censo2017 import censo_ruta

class TestSimple(unittest.TestCase) :
    def test_censo_ruta(self) :
        self.assertStringMatchs(sub(r'^.*?/', '/', censo_ruta()), '/.censo2017')

if __name__ == '__main__':
    unittest.main()
