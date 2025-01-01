import random
import matplotlib.pyplot as plt

class GameEngine:
    def __init__(self):
        """
        Initialise le moteur de simulation.
        """
        self.map = self.generate_map(10, 10)
        self.units = []
        self.resources = {'gold': 1000, 'food': 1000}

    def generate_map(self, width, height):
        """
        Génère une carte sous forme de grille abstraite.
        """
        return [['empty' for _ in range(width)] for _ in range(height)]

    def add_unit(self, unit):
        """
        Ajoute une unité avec une position aléatoire sur la carte.
        """
        self.units.append(unit)
        unit['position'] = [random.randint(0, 9), random.randint(0, 9)]

    def move_unit(self, unit, new_position):
        """
        Déplace une unité sur la carte.
        """
        x, y = new_position
        if 0 <= x < len(self.map) and 0 <= y < len(self.map[0]):
            unit['position'] = [x, y]

    def battle(self, attacker, defender):
        """
        Simule une bataille entre deux unités.
        """
        print(f"Battle: {attacker['id']} attacks {defender['id']}")
        attacker_damage = random.randint(10, 30)
        defender_damage = random.randint(5, 25)

        defender['hp'] -= attacker_damage
        attacker['hp'] -= defender_damage

        if defender['hp'] <= 0:
            print(f"Defender {defender['id']} defeated!")
            self.units.remove(defender)
        if attacker['hp'] <= 0:
            print(f"Attacker {attacker['id']} defeated!")
            self.units.remove(attacker)

    def collect_resources(self, unit):
        """
        Simule la collecte de ressources par une unité.
        """
        if unit['status'] == 'working':
            self.resources['gold'] += 10
            self.resources['food'] += 5
            print(f"Unit {unit['id']} collected resources.")

    def update(self):
        """
        Met à jour l'état du moteur à chaque tour.
        """
        for unit in self.units:
            if unit['status'] == 'working':
                self.collect_resources(unit)

        for i, unit in enumerate(self.units):
            for j, other_unit in enumerate(self.units):
                if i != j and unit['team'] != other_unit['team']:
                    if abs(unit['position'][0] - other_unit['position'][0]) <= 1 and \
                            abs(unit['position'][1] - other_unit['position'][1]) <= 1:
                        self.battle(unit, other_unit)

    def visualize(self):
        """
        Visualise les positions des unités sur la carte.
        """
        colors = {'team_1': 'blue', 'team_2': 'red', 'team_3': 'green'}
        plt.figure(figsize=(6, 6))
        plt.xlim(0, len(self.map))
        plt.ylim(0, len(self.map[0]))

        for unit in self.units:
            team = unit['team']
            x, y = unit['position']
            plt.scatter(x, y, c=colors.get(team, 'black'), label=team, s=100)

        plt.title("Unit Positions")
        plt.legend(loc='upper right')
        plt.grid(True)
        plt.show()
