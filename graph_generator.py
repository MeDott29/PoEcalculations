import matplotlib.pyplot as plt
from arpg_mechanics import ARPGMechanics


def generate_graph(crit_chance, max_frenzy, bow_speed, time):
    """
    Generates a graph representing bow attacks over time, arrows per bow attack, and frenzy charges generated per attack.

    Parameters:
    crit_chance (float): The chance of a critical hit.
    max_frenzy (int): The maximum number of frenzy charges.
    bow_speed (float): The speed of the bow.
    time (int): The time over which to simulate combat.

    Returns:
    matplotlib.figure.Figure: The generated graph.
    """
    arpg = ARPGMechanics(crit_chance, max_frenzy, bow_speed)

    times = list(range(time + 1))
    arrows = []
    frenzy_charges = []

    for t in times:
        a, f = arpg.simulate_combat(t)
        arrows.append(a)
        frenzy_charges.append(f)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('arrows', color=color)
    ax1.plot(times, arrows, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('frenzy charges', color=color)
    ax2.plot(times, frenzy_charges, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Bow Attacks and Frenzy Charges Over Time')
    return fig
