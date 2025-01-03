import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        petr = Runner('Петр')
        for _ in range(10):
            petr.walk()
        self.assertEqual(petr.distance, 50)

    def test_run(self):
        ivan = Runner('Иван')
        for _ in range(10):
            ivan.run()
        self.assertEqual(ivan.distance, 100)

    def test_challenge(self):
        jack = Runner('Jack')
        bob = Runner('Bob')
        for _ in range(10):
            jack.run()
            bob.walk()
        self.assertNotEqual(jack.distance, 200)
        self.assertNotEqual(bob.distance, 300)


if __name__ == '__main__':
    unittest.main()










