import unittest

from init import Projectile, Target


class ARPGMechanics:
    def __init__(self, crit_chance, max_frenzy, bow_speed):
        self.crit_chance = crit_chance
        self.max_frenzy = max_frenzy
        self.bow_speed = bow_speed

    def calculate_frenzy_charges(self, crit_hits):
        return crit_hits * (0.2 - 0.4)

    def calculate_arrows_per_attack(self, frenzy_charges):
        return 1 + frenzy_charges

    def simulate_combat(self, time):
        arrows = 0
        frenzy_charges = 0
        for _ in range(int(time * self.bow_speed)):
            crit_hits = self.crit_chance
            frenzy_charges += self.calculate_frenzy_charges(crit_hits)
            frenzy_charges = min(frenzy_charges, self.max_frenzy)
            arrows += self.calculate_arrows_per_attack(frenzy_charges)
        return arrows, frenzy_charges

class TestARPGMechanics(unittest.TestCase):
    def setUp(self):
        self.arpg = ARPGMechanics(0.5, 5, 1)

    def test_calculate_frenzy_charges(self):
        self.assertEqual(self.arpg.calculate_frenzy_charges(2), 0.4)

    def test_calculate_arrows_per_attack(self):
        self.assertEqual(self.arpg.calculate_arrows_per_attack(3), 4)

    def test_simulate_combat(self):
        arrows, frenzy_charges = self.arpg.simulate_combat(10)
        self.assertEqual(arrows, 40)
        self.assertEqual(frenzy_charges, 5)

if __name__ == '__main__':
    unittest.main()
