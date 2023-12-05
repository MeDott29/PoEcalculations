
from scenario import intersects, calculate_trajectory

# Calculations specific to the ARPG mechanics will be handled in 'arpg_mechanics.py'.
# The following function is part of the old mechanic and is kept for legacy purposes.
def projectile_collision(projectile, target):
    # Calculate the trajectory of the projectile
    trajectory = calculate_trajectory(projectile)

    # Check if the trajectory intersects with the target
    if intersects(trajectory, target):
        return True  # Collision occurred
    else:
        return False  # No collision

