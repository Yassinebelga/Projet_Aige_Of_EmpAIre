from game_engine import GameEngine
from ai_profiles import assign_units_for_attack, update_strategy

# Initialisation du moteur
engine = GameEngine()

# Définir plusieurs IA
contexts = [
    {'team': 'team_1', 'strategy': 'aggressive', 'intensity': 0.8},
    {'team': 'team_2', 'strategy': 'defensive', 'intensity': 0.4},
]

# Ajouter des unités
for context in contexts:
    for i in range(5):
        engine.add_unit({'id': f"{context['team']}_unit_{i+1}", 'team': context['team'], 'type': 'soldier', 'hp': 100, 'status': 'idle'})

# Simulation
for turn in range(10):
    print(f"\n--- Turn {turn + 1} ---")
    for context in contexts:
        # Mettre à jour la stratégie
        update_strategy(context, engine)

        # Appliquer les actions selon la stratégie
        if context['strategy'] == 'aggressive':
            assign_units_for_attack(context, engine)

    # Mise à jour du moteur
    engine.update()

    # Visualiser la carte
    engine.visualize()
