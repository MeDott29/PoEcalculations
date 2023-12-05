import matplotlib.pyplot as plt


def generate_graphs(attacks_per_second, crit_chance, additional_arrows):
    fig, ax = plt.subplots()
    
    ax.plot(attacks_per_second, additional_arrows, label='Attacks per Second')
    ax.plot(crit_chance, additional_arrows, label='Critical Strike Chance')
    
    ax.set_xlabel('Attacks per Second / Critical Strike Chance')
    ax.set_ylabel('Additional Arrows Fired')
    ax.set_title('Relationship between Attacks per Second / Critical Strike Chance and Additional Arrows Fired')
    
    ax.legend()
    
    plt.savefig('graph.png')
