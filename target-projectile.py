from init import intersects
from init import calculate_trajectory
from battle import create_battle
# Calculations specific to the ARPG mechanics will be handled in 'arpg_mechanics.py'.
# The following function is part of the old mechanic and is kept for legacy purposes.
def projectile_collision(projectile, target):
    # Calculate the trajectory of the projectile
    trajectory = calculate_trajectory(projectile)

    # battle_scenario = create_battle(bow, enemies)
    # Calculate the trajectory of the projectile
    trajectory = calculate_trajectory(projectile)
    # Check if the trajectory intersects with the target
    collision, impact_force = projectile_collision(projectile, target)
    if collision:
        return True  # Collision occurred
    else:
        return False  # No collision
