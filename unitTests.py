import unittest
import __init__ as ln2sqlmodule


class Testln2sql(unittest.TestCase):

    def test_getSql(self):
        tests = [
            {
                'input': "emp",
                'output': "SELECT * FROM emp;"
            },
        ]

        for test in tests:
            self.assertEqual(
                str(ln2sqlmodule.getSql(test['input'],'emp.sql')), test['output'])

    def test_getSql_like(self):
        tests = [
            {
                'input': "emp",
                'output': "SELECT * FROM emp;"
            },
        ]

        for test in tests:
            self.assertEqual(
                str(ln2sqlmodule.getSql_like(test['input'],'emp.sql')), test['output'])

if __name__ == '__main__':
    unittest.main()
