import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        TournamentTest.all_results['Участники: Усейн и Ник'] = result

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        TournamentTest.all_results['Участники: Андрей и Ник'] = result

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        TournamentTest.all_results['Участники: Усейн, Андрей и Ник'] = result


    @classmethod
    def tearDownClass(cls):
        print("Результаты всех тестов:")
        for key, results in cls.all_results.items():
            formatted_res = {place: str(participant) for place, participant in results.items()}
            print(f"{key}: {formatted_res}")


if __name__ == '__main__':
        unittest.main()



