from decision_tree import DecisionNode
import random

def is_aggressive(context):
    return context.get('strategy', 'defensive') == 'aggressive'

def is_defensive(context):
    return context.get('strategy', 'defensive') == 'defensive'

def assign_units_for_attack(context, engine):
    attacking_units = []
    reserved_units = []
    intensity = context.get('intensity', 0.5)

    for unit in engine.units:
        if unit['team'] == context['team'] and unit['status'] == 'idle':
            if random.random() < intensity:
                unit['status'] = 'attacking'
                attacking_units.append(unit)
            else:
                unit['status'] = 'defending'
                reserved_units.append(unit)

    return attacking_units, reserved_units

def update_strategy(context, engine):
    """
    Met à jour la stratégie de l'IA en fonction de l'état actuel.
    """
    team_units = [unit for unit in engine.units if unit['team'] == context['team']]
    resource_status = engine.resources['gold'] > 200 and engine.resources['food'] > 100
    strong_army = len(team_units) >= 5

    if not resource_status or len(team_units) < 3:
        context['strategy'] = 'defensive'
        context['intensity'] = 0.4
    elif resource_status and strong_army:
        context['strategy'] = 'aggressive'
        context['intensity'] = 0.8
    else:
        context['strategy'] = 'balanced'
        context['intensity'] = 0.6
