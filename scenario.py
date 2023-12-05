from arpg_mechanics import ARPGMechanics
from init import (Projectile, Target, calculate_impact_force,
                  calculate_trajectory, intersects)
from target_projectile import projectile_collision


def main():
    # Create an instance of Projectile
    projectile = Projectile(mass=10, velocity=20, angle=45)

    # Create an instance of Target
    target = Target(position=(0, 0), size=5)

    # Calculate the trajectory of the projectile
    trajectory = calculate_trajectory(projectile)

    # Check if the trajectory intersects with the target
    if intersects(trajectory, target):
        print("Collision occurred")

        # Calculate the impact force
        impact_force = calculate_impact_force(projectile, target)
        print("Impact force:", impact_force)
    else:
        print("No collision")

if __name__ == "__main__":
    main()
