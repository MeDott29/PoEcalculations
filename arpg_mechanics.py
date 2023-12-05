# Helper functions for code modification. Run exec() on this file to load the functions into memory.
import ast
import difflib

file_path = '/mnt/data/file-dv55U9OWyTNM7SWuCTPvBMve'
with open(file_path, 'r') as file:
    file_content = file.read()
original_lines = file_content.splitlines()
current_content = file_content

def print_original_lines(i, j):
    """
    Displays the original lines between line numbers i and j.
    """
    start = max(0, i - 10)
    end = min(len(original_lines), j + 10)

    for index in range(start, end):
        if index == i:
            print("\n--- Start of snippet ---")
        elif index == j:
            print("--- End of snippet ---\n")

        print(f"{index}: {original_lines[index]}")
    print("\n")

def print_original_lines_with_keywords(keywords):
    """
    Displays the original lines between line numbers i and j when any of the keywords are found.
    Use single words.
    """
    context = 10

    matches = [i for i, line in enumerate(original_lines) if any(keyword in line.lower() for keyword in keywords)]
    expanded_matches = set()

    for match in matches:
        start = max(0, match - context)
        end = min(len(original_lines), match + context + 1)
        for i in range(start, end):
            expanded_matches.add(i)

    for i in sorted(expanded_matches):
        print(f"{i}: {original_lines[i]}")

def check_valid_python(code):
    """
    Check if the code is valid python using ast.parse. Use this to check if python code is valid after making edits.
    """
    try:
        # Check for valid python
        ast.parse(code)
        print("Python code is valid.")
    except SyntaxError as e:
        print("SyntaxError:", e)

def print_diff(new_content, old_content=file_content, final_diff=False):
    if new_content == old_content:
        print("No changes were made. Please try again to produce a valid diff.")
    unified_diff = difflib.unified_diff(
        old_content.split("\n"), new_content.split("\n")
    )
    unified_diff_str = '\n'.join([diff_line.strip("\n") for diff_line in unified_diff])
    if final_diff:
        print(f"<final_diff>\n{unified_diff_str}\n
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

