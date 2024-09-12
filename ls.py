import tor
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        first = tor.Runner('Alex')
        for i in range(10):
            first.walk()
        self.assertEqual(first.distance, 50)

    def test_run(self):
        second = tor.Runner('Sergay')
        for i in range(10):
            second.run()
        self.assertEqual(second.distance, 100)

    def test_challenge(self):
        first = tor.Runner('Alex')
        second = tor.Runner('Sergay')
        for i in range(10):
            first.walk()
            second.run()
        self.assertNotEqual(first.distance, second.distance)

if __name__ == '__main__':
    unittest.main()