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

    def test_calculate_frenzy_charges_zero(self):
        self.assertEqual(self.arpg.calculate_frenzy_charges(0), 0, "Frenzy charges should be zero with zero crit hits.")

    def test_calculate_frenzy_charges_negative(self):
        self.assertEqual(self.arpg.calculate_frenzy_charges(-1), -0.2, "Frenzy charges should be negative with negative crit hits.")

    def test_calculate_frenzy_charges_max_frenzy(self):
        excess_frenzy_charges = self.arpg.max_frenzy + 1
        self.assertEqual(self.arpg.calculate_frenzy_charges(excess_frenzy_charges), self.arpg.max_frenzy,
                         "Frenzy charges should not exceed max_frenzy value.")

    def test_calculate_arrows_per_attack(self):
        self.assertEqual(self.arpg.calculate_arrows_per_attack(3), 4)

    def test_calculate_arrows_per_attack_zero(self):
        self.assertEqual(self.arpg.calculate_arrows_per_attack(0), 1, "Should always fire at least one arrow.")

    def test_simulate_combat(self):
        arrows, frenzy_charges = self.arpg.simulate_combat(10)
        self.assertEqual(arrows, 40)
        self.assertEqual(frenzy_charges, 5)

    def test_simulate_combat_high_values(self):
        high_crit_chance_arpg = ARPGMechanics(0.9, 20, 2)
        arrows, frenzy_charges = high_crit_chance_arpg.simulate_combat(10)
        # Calculate expected values, the exact number may be needed here based on actual game mechanics.
        # Using placeholders for now.
        expected_arrows = 100 # Placeholder, should be actual calculated value
        expected_frenzy_charges = 20 # Placeholder, should be actual calculated value

    def test_simulate_combat_zero_time(self):
        arrows, frenzy_charges = self.arpg.simulate_combat(0)
        self.assertEqual(arrows, 0, "No arrows should be fired with zero time.")
        self.assertEqual(frenzy_charges, 0, "No frenzy charges should be gained with zero time.")

    def test_init_arpg_mechanics(self):
        arpg_custom = ARPGMechanics(0.25, 3, 0.75)
        self.assertEqual(arpg_custom.crit_chance, 0.25, "Critical chance should be set correctly.")
        self.assertEqual(arpg_custom.max_frenzy, 3, "Max frenzy should be set correctly.")
        self.assertEqual(arpg_custom.bow_speed, 0.75, "Bow speed should be set correctly.")
        self.assertEqual(arrows, expected_arrows, "Arrows fired should match expected value for high crit_chance.")
        self.assertEqual(frenzy_charges, expected_frenzy_charges, "Frenzy charges should match expected value for high max_frenzy.")

if __name__ == '__main__':
    unittest.main()

