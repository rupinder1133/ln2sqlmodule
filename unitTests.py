import unittest
import __init__ as ln2sqlmodule


class Testln2sql(unittest.TestCase):

    def test_getSql(self):
        tests = [
            {
                "input": "emp",
                "output": "SELECT * FROM emp;"
            },
            {
                "input": "name of all emp",
                "output": "SELECT emp.name FROM emp;"
            },
            {
                "input": "name and score for emp with id = 2",
                "output": "SELECT emp.name, emp.score FROM emp WHERE emp.id = '2';"
            },
            {
                "input": "all data for city where cityName = 'pune'",
                "output": "SELECT * FROM city WHERE city.cityName = 'pune';"  
            },
            {
                "input": "cityName for emp",
                "output": "SELECT city.cityName FROM emp INNER JOIN city ON emp.cityId = city.id;"
            },
            {
                "input": "cityName for emp with id = 2",
                "output": "SELECT city.cityName FROM emp INNER JOIN city ON emp.cityId = city.id WHERE emp.id = '2';"
            },
            {
                "input": "cityName and score for emp with id = 2",
                "output": "SELECT city.cityName, emp.score FROM emp INNER JOIN city ON emp.cityId = city.id WHERE emp.id = '2';"
            },

        ]

        for test in tests:
            self.assertEqual(
                str(ln2sqlmodule.getSql(test['input'],'emp.sql')), test['output'])

    def test_getSql_like(self):
        tests = [
            {
                "input": "emp",
                "output": "SELECT * FROM emp;"
            },
            {
                "input": "name of all emp",
                "output": "SELECT emp.name FROM emp;"
            },
            {
                "input": "name and score for emp with name = rupinder",
                "output": "SELECT emp.name, emp.score FROM emp WHERE emp.name LIKE '%rupinder%';"
            },
            {
                "input": "all data for city where cityName is 'pune'",
                "output": "SELECT * FROM city WHERE city.cityName LIKE '%pune%';"  
            },
            {
                "input": "cityName for emp",
                "output": "SELECT city.cityName FROM emp INNER JOIN city ON emp.cityId = city.id;"
            },
            {
                "input": "cityName for emp with name is 'rupinder singh'",
                "output": "SELECT city.cityName FROM emp INNER JOIN city ON emp.cityId = city.id WHERE emp.name LIKE '%rupinder%singh%';"
            },
            {
                "input": "cityName and score for emp with score = 2",
                "output": "SELECT city.cityName, emp.score FROM emp INNER JOIN city ON emp.cityId = city.id WHERE emp.score LIKE '%2%';"
            }
        ]

        for test in tests:
            self.assertEqual(
                str(ln2sqlmodule.getSql_like(test['input'],'emp.sql')), test['output'])

if __name__ == '__main__':
    unittest.main()
